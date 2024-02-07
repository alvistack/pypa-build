# Copyright 2024 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-build
Epoch: 100
Version: 1.2.0
Release: 1%{?dist}
BuildArch: noarch
Summary: A simple, correct Python build frontend
License: MIT
URL: https://github.com/pypa/build/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
A simple, correct Python build frontend.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-build
Summary: A simple, correct Python build frontend
Requires: python3
Requires: python3-importlib-metadata >= 4.6
Requires: python3-packaging >= 19.1
Requires: python3-pyproject-hooks
Requires: python3-tomli >= 1.1.0
Provides: python3-build = %{epoch}:%{version}-%{release}
Provides: python3dist(build) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-build = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(build) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-build = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(build) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-build
A simple, correct Python build frontend.

%files -n python%{python3_version_nodots}-build
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-build
Summary: A simple, correct Python build frontend
Requires: python3
Requires: python3-importlib-metadata >= 4.6
Requires: python3-packaging >= 19.1
Requires: python3-pyproject-hooks
Requires: python3-tomli >= 1.1.0
Provides: python3-build = %{epoch}:%{version}-%{release}
Provides: python3dist(build) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-build = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(build) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-build = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(build) = %{epoch}:%{version}-%{release}

%description -n python3-build
A simple, correct Python build frontend.

%files -n python3-build
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-build
Summary: A simple, correct Python build frontend
Requires: python3
Requires: python3-importlib-metadata >= 4.6
Requires: python3-packaging >= 19.1
Requires: python3-pyproject-hooks
Requires: python3-tomli >= 1.1.0
Provides: python3-build = %{epoch}:%{version}-%{release}
Provides: python3dist(build) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-build = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(build) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-build = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(build) = %{epoch}:%{version}-%{release}

%description -n python3-build
A simple, correct Python build frontend.

%files -n python3-build
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%changelog
