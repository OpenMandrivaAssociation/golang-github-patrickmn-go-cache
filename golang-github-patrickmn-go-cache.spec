# Run tests in check section
%bcond_with check

# https://github.com/patrickmn/go-cache
%global goipath         github.com/patrickmn/go-cache
Version:                2.1.0

%gometa

Name:           golang-github-patrickmn-go-cache
Release:        4%{?dist}
Summary:        An in-memory key:value store/cache library for Go
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{summary}


%package devel
Summary:       %{summary}
BuildArch:     noarch


%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md CONTRIBUTORS


%changelog
* Sat Oct 06 2018 Robert-André Mauchin <zebob.m@gmail.com> - 2.1.0-4
- Update to new Go packaging

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Oct 07 2017 Ed Marshall <esm@logic.net> - 2.1.0-1
- Update to upstream 2.1.0 release.

* Sat Oct 07 2017 Ed Marshall <esm@logic.net> - 2.0.0-1
- First package for Fedora


