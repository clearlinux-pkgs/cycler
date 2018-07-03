#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cycler
Version  : 0.10.0
Release  : 20
URL      : https://github.com/matplotlib/cycler/archive/v0.10.0.tar.gz
Source0  : https://github.com/matplotlib/cycler/archive/v0.10.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: cycler-python3
Requires: cycler-python
Requires: six
BuildRequires : pbr
BuildRequires : pip

BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six

%description
cycler: composable cycles
=========================
Docs: http://matplotlib.org/cycler/

%package python
Summary: python components for the cycler package.
Group: Default
Requires: cycler-python3

%description python
python components for the cycler package.


%package python3
Summary: python3 components for the cycler package.
Group: Default
Requires: python3-core

%description python3
python3 components for the cycler package.


%prep
%setup -q -n cycler-0.10.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523287573
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
