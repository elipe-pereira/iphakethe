#!/usr/bin/python3
# coding: utf-8
import os


class Repo(object):
    def __init__(self):
        self.__dest_linux_distro_repo = ""
        self.__codename_repo = ""
        self.__distro_repo = ""

    def set_dest_linux_distro_repo(self, folder_dest):
        self.__dest_linux_distro_repo = folder_dest

    def set_codename_repo(self, codename):
        self.__codename_repo = codename

    def set_distro_repo(self, distro_repo):
        self.__distro_repo = distro_repo

    def send_to_repo(self, package_file_name, keep_old_packages):
        if keep_old_packages == "yes":
            os.system("reprepro --keepunreferencedfiles -b {0}/{1} includedeb {2} {3}.deb".format(
                self.__dest_linux_distro_repo,
                self.__distro_repo,
                self.__codename_repo,
                package_file_name))

        else:
            os.system("reprepro -b {0}/{1} includedeb {2} {3}.deb".format(
                self.__dest_linux_distro_repo,
                self.__distro_repo,
                self.__codename_repo,
                package_file_name))
