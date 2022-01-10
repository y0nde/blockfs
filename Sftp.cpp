#include "Sftp.h"

void convert_sf_to_St(std::string path,sftp_attributes sfbuf,Stat &stat){
	stat.name = path;
	stat.size = sfbuf->size;
	stat.mtime = sfbuf->mtime;
	stat.atime = sfbuf->atime;
}

int sftp::loadoption(){
	int index;
	std::string line,key;
	ConfigPath = std::filesystem::current_path().string() + "/config/sshconfig";
	std::ifstream ifs;
	ifs.open(ConfigPath);
	if(!ifs){
		std::cerr << "open sshconfig failed" << std::endl;
	}
	while(std::getline(ifs,line)){
		index = line.find(" ");
		key=line.substr(0,line.find(" "));
		if(key=="host"){
			host = line.substr(index+1);
		}else if(key=="username"){
			username = line.substr(index+1);
		}else if(key=="password"){
			password = line.substr(index+1);
		}
	}
	return 0;
}

sftp::sftp(){
	if(loadoption()!=0){
		std::cerr << "loadoption failed: " << ssh_get_error(m_ssh) << std::endl;
	}
	m_ssh = ssh_new();
	ssh_options_set(m_ssh, SSH_OPTIONS_HOST, host.c_str());
	if(ssh_connect(m_ssh)!=SSH_OK){
		ssh_free(m_ssh);
		std::cerr << "ssh_connect failed: " << ssh_get_error(m_ssh) << std::endl;
	}
	std::cout << "connect success" << std::endl;
	if(ssh_userauth_password(m_ssh,username.c_str(),password.c_str())!=SSH_AUTH_SUCCESS){
		std::cerr << "ssh_userauth_password failed: " << ssh_get_error(m_ssh) << std::endl;
		ssh_free(m_ssh);
	}
	std::cout << "auth success" << std::endl;
	m_sftp = sftp_new(m_ssh);
	if(sftp_init(m_sftp)!=SSH_OK){
		std::cerr << "sftp_init failed: " << ssh_get_error(m_ssh) << std::endl;
		sftp_free(m_sftp);
		ssh_free(m_ssh);
	}
	std::cout << "sftp_init success" << std::endl;
}

sftp::~sftp(){
	sftp_free(m_sftp);
	ssh_disconnect(m_ssh);
	ssh_free(m_ssh);
}

Stat sftp::getstat(std::string path){
	Stat attr;
	sftp_attributes sfbuf;
	sfbuf = sftp_stat(m_sftp,path.c_str());
	if(!sfbuf){
		std::cerr << "sftp_stat failed" << std::endl;
	}
	std::cout << "sftp_stat success" << std::endl;
	convert_sf_to_St(path,sfbuf,attr);
	std::cout << "convert success" << std::endl;
	return attr;
}

std::list<Stat> sftp::getdir(std::string path){
	std::list<Stat> attrs;
	Stat attr;
	sftp_attributes sfbuf;
	sftp_dir dir;
	dir = sftp_opendir(m_sftp,path.c_str());
	if(!dir){
		std::cerr << "getdir open " << path << " failed" << std::endl;
		return attrs; 
	}
	sfbuf=sftp_readdir(m_sftp,dir);
	while(sfbuf!=NULL){
		convert_sf_to_St(sfbuf->name,sfbuf,attr);
		attrs.push_back(attr);
		sftp_attributes_free(sfbuf);
		sfbuf=sftp_readdir(m_sftp,dir);
	}
	sftp_closedir(dir);
	return attrs;
}

int sftp::download(std::string from, std::string dest){
	sftp_file file;
	int nbytes,size=0;
	std::ofstream ofs;
	char buffer[512];
	file = sftp_open(m_sftp,from.c_str(), O_RDONLY,0);
	ofs.open(dest,std::ios_base::out|std::ios_base::binary|std::ios_base::trunc);
	for(;;){
		nbytes = sftp_read(file,buffer,sizeof(buffer));
		if(nbytes==0){
			break;
		}else if(nbytes<0){
			std::cerr << "sftp_read error" << std::endl;
			sftp_close(file);
			return -1;
		}
		ofs.write(buffer, nbytes);
		if(ofs.bad()){
			std::cerr << "ofs write error" << std::endl;
			return -1;
		}
		size += nbytes;
	}
	return size;
}
