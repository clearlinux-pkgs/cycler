#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cycler
Version  : 0.10.0
Release  : 9
URL      : https://github.com/matplotlib/cycler/archive/v0.10.0.tar.gz
Source0  : https://github.com/matplotlib/cycler/archive/v0.10.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: cycler-legacypython
Requires: cycler-python
Requires: six
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six

%description
cycler: composable cycles
=========================
Docs: http://matplotlib.org/cycler/

%package legacypython
Summary: legacypython components for the cycler package.
Group: Default

%description legacypython
legacypython components for the cycler package.


%package python
Summary: python components for the cycler package.
Group: Default
Requires: cycler-legacypython

%description python
python components for the cycler package.


%prep
%setup -q -n cycler-0.10.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1505001695
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1505001695
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)
/usr/lib/python3*/*
