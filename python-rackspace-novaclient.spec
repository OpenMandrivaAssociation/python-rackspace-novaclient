Name:		python-rackspace-novaclient
Version:	2.1
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/r/rackspace-novaclient/rackspace-novaclient-%{version}.tar.gz
Summary:	Metapackage to install python-novaclient and Rackspace extensions
URL:		https://pypi.org/project/rackspace-novaclient/
License:	Apache License, Version 2.0
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
Metapackage to install python-novaclient and Rackspace extensions

%files
%{py_sitedir}/rackspace_novaclient-*.*-info
