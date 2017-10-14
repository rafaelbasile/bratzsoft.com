import os
import pip
import datetime
from subprocess import call


def get_outdated():
	list_command = pip.commands.list.ListCommand()
	options, args = list_command.parse_args([])
	packages = pip.utils.get_installed_distributions()
	return list_command.get_outdated(packages, options)


def upgrade_outdated(all_pkgs=False):
	packages_upgraded = []	
	if all_pkgs:
		to_upgrade = get_packages(upgrade=True)
	else:
		to_upgrade = get_outdated()
	for dist in get_outdated():
		call ("pip install --upgrade {pack_name}".format(pack_name=dist.project_name), shell=True)
		packages_upgraded.append(dist.project_name)

	if len(packages_upgraded) > 0:
		print("Upgraded the following packages:\n")
		for pkg in packages_upgraded:
			print(" - " + str(pkg))


def save_archive(archive_list):
	requirements_path = os.path.join(os.getcwd(), "requirements")
	if not os.path.exists(requirements_path):
		os.mkdir(requirements_path)
	today = str(datetime.datetime.today().strftime("%Y%m%d-%H%M%S"))
	filepath = os.path.join(requirements_path, "requirements__%s.txt" %(today))
	with open(filepath, "w+") as archive:
		for rq in sorted(archive_list, key=str.lower):
			archive.write(str(rq) + "\n")
	print("Archive done")


def make_archive():
	print("Making archive...")
	current = get_packages()
	save_archive(current)


def get_packages(upgrade=False):
	print("Getting Packages...")	
	current = []
	for dist in pip.get_installed_distributions():
		if upgrade:
			current.append(dist)
		else:
			current.append(str(dist.as_requirement()))	
	return current


def get_requirements_location(next_to=None):
	location = os.path.join(os.getcwd(), "requirements.txt")
	if next_to is not None:
		location = None
		for root, dirs, files in os.walk(os.getcwd()):
			for file in files:
				if str(file) ==str(next_to):
					location = os.path.join(root, "requirements.txt")
					return location
	return None

def save_requirements(next_to='manage.py'):
	packages = get_packages()
	print("Saving Requirements...")
	location = get_requirements_location(next_to=next_to)
	with open(location, "w") as f:
		for pkg in sorted(packages, key=str.lower):
			f.write(str(pkg) + "\n")
	print("Requirements saved")


make_archive()
upgrade_outdated(all_pkgs=False)
save_requirements()