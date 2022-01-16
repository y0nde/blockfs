#ifndef ENTRY_H
#define ENTRY_H
#include <iostream>
#include <fstream>
#include <string>
#include <filesystem>
#include <list>
#include <vector>
#include <fcntl.h>
#include <sys/stat.h>
#include "Sftp.h"
#include "Block.h"

class attribute {
private:
	sftp* p_sftp;
	struct stat* st;
public:
	std::string path;
	std::string name;

	attribute(sftp* _p_sftp,std::string _path);
	attribute(sftp* _p_sftp,std::string _path,struct stat &_st);
	~attribute();
	struct stat* getattr();
	void print();
	int download();
};

class entry {
protected:
	std::string path;
	int offset;
	attribute* stat;
	sftp* p_sftp;
public:
	entry(std::string _path,sftp *_p_sftp);
	entry(std::string _path,struct stat &_st,sftp *_p_sftp);
	struct stat* getattr();
	virtual ~entry();
};

class directory: public entry{
private:
	std::list<attribute*> attrs;
public:
	directory(std::string _path,sftp *_p_sftp);
	directory(std::string _path,struct stat &_st,sftp *_p_sftp);
	~directory();
	std::list<attribute*> readdir();
	void ls();
	void download();
};

class file: public entry{
private:
	std::vector<block*> blocks;
	bool haveAll;
	bool fd;
	int lock;
public:
	file(std::string _path,sftp *_p_sftp);
	file(std::string _path,struct stat &_st,sftp *_p_sftp);
	~file();
	bool isopen();
	int open();
	int close();
	int read(char* buf,int offset,int size);
	int write(char* buf,int offset,int size);
};

#endif
