#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-tzdb
Version  : 0.3.0
Release  : 10
URL      : https://cran.r-project.org/src/contrib/tzdb_0.3.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/tzdb_0.3.0.tar.gz
Summary  : Time Zone Database Information
Group    : Development/Tools
License  : MIT
Requires: R-tzdb-lib = %{version}-%{release}
Requires: R-cpp11
BuildRequires : R-cpp11
BuildRequires : buildreq-R

%description
Authority (IANA) Time Zone Database. It is updated periodically to
    reflect changes made by political bodies to time zone boundaries, UTC
    offsets, and daylight saving time rules. Additionally, this package
    provides a C++ interface for working with the 'date' library. 'date'
    provides comprehensive support for working with dates and date-times,
    which this package exposes to make it easier for other R packages to
    utilize. Headers are provided for calendar specific calculations,
    along with a limited interface for time zone manipulations.

%package lib
Summary: lib components for the R-tzdb package.
Group: Libraries

%description lib
lib components for the R-tzdb package.


%prep
%setup -q -c -n tzdb
cd %{_builddir}/tzdb

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1648500280

%install
export SOURCE_DATE_EPOCH=1648500280
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library tzdb
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library tzdb
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library tzdb
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc tzdb || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/tzdb/DESCRIPTION
/usr/lib64/R/library/tzdb/INDEX
/usr/lib64/R/library/tzdb/LICENSE
/usr/lib64/R/library/tzdb/Meta/Rd.rds
/usr/lib64/R/library/tzdb/Meta/features.rds
/usr/lib64/R/library/tzdb/Meta/hsearch.rds
/usr/lib64/R/library/tzdb/Meta/links.rds
/usr/lib64/R/library/tzdb/Meta/nsInfo.rds
/usr/lib64/R/library/tzdb/Meta/package.rds
/usr/lib64/R/library/tzdb/NAMESPACE
/usr/lib64/R/library/tzdb/NEWS.md
/usr/lib64/R/library/tzdb/R/tzdb
/usr/lib64/R/library/tzdb/R/tzdb.rdb
/usr/lib64/R/library/tzdb/R/tzdb.rdx
/usr/lib64/R/library/tzdb/help/AnIndex
/usr/lib64/R/library/tzdb/help/aliases.rds
/usr/lib64/R/library/tzdb/help/paths.rds
/usr/lib64/R/library/tzdb/help/tzdb.rdb
/usr/lib64/R/library/tzdb/help/tzdb.rdx
/usr/lib64/R/library/tzdb/html/00Index.html
/usr/lib64/R/library/tzdb/html/R.css
/usr/lib64/R/library/tzdb/include/date/chrono_io.h
/usr/lib64/R/library/tzdb/include/date/date.h
/usr/lib64/R/library/tzdb/include/date/ios.h
/usr/lib64/R/library/tzdb/include/date/islamic.h
/usr/lib64/R/library/tzdb/include/date/iso_week.h
/usr/lib64/R/library/tzdb/include/date/julian.h
/usr/lib64/R/library/tzdb/include/date/ptz.h
/usr/lib64/R/library/tzdb/include/date/solar_hijri.h
/usr/lib64/R/library/tzdb/include/date/tz.h
/usr/lib64/R/library/tzdb/include/date/tz_private.h
/usr/lib64/R/library/tzdb/include/tzdb/date.h
/usr/lib64/R/library/tzdb/include/tzdb/defines.h
/usr/lib64/R/library/tzdb/include/tzdb/islamic.h
/usr/lib64/R/library/tzdb/include/tzdb/iso_week.h
/usr/lib64/R/library/tzdb/include/tzdb/julian.h
/usr/lib64/R/library/tzdb/include/tzdb/ptz.h
/usr/lib64/R/library/tzdb/include/tzdb/solar_hijri.h
/usr/lib64/R/library/tzdb/include/tzdb/tz.h
/usr/lib64/R/library/tzdb/include/tzdb/tzdb.h
/usr/lib64/R/library/tzdb/tests/testthat.R
/usr/lib64/R/library/tzdb/tests/testthat/_snaps/path.md
/usr/lib64/R/library/tzdb/tests/testthat/test-initialize.R
/usr/lib64/R/library/tzdb/tests/testthat/test-names.R
/usr/lib64/R/library/tzdb/tests/testthat/test-path.R
/usr/lib64/R/library/tzdb/tests/testthat/test-version.R
/usr/lib64/R/library/tzdb/tzdata/CONTRIBUTING
/usr/lib64/R/library/tzdb/tzdata/LICENSE
/usr/lib64/R/library/tzdb/tzdata/Makefile
/usr/lib64/R/library/tzdb/tzdata/NEWS
/usr/lib64/R/library/tzdb/tzdata/README
/usr/lib64/R/library/tzdb/tzdata/SECURITY
/usr/lib64/R/library/tzdb/tzdata/africa
/usr/lib64/R/library/tzdb/tzdata/antarctica
/usr/lib64/R/library/tzdb/tzdata/asia
/usr/lib64/R/library/tzdb/tzdata/australasia
/usr/lib64/R/library/tzdb/tzdata/backward
/usr/lib64/R/library/tzdb/tzdata/backzone
/usr/lib64/R/library/tzdb/tzdata/calendars
/usr/lib64/R/library/tzdb/tzdata/checklinks.awk
/usr/lib64/R/library/tzdb/tzdata/checktab.awk
/usr/lib64/R/library/tzdb/tzdata/etcetera
/usr/lib64/R/library/tzdb/tzdata/europe
/usr/lib64/R/library/tzdb/tzdata/factory
/usr/lib64/R/library/tzdb/tzdata/iso3166.tab
/usr/lib64/R/library/tzdb/tzdata/leap-seconds.list
/usr/lib64/R/library/tzdb/tzdata/leapseconds
/usr/lib64/R/library/tzdb/tzdata/leapseconds.awk
/usr/lib64/R/library/tzdb/tzdata/northamerica
/usr/lib64/R/library/tzdb/tzdata/southamerica
/usr/lib64/R/library/tzdb/tzdata/theory.html
/usr/lib64/R/library/tzdb/tzdata/version
/usr/lib64/R/library/tzdb/tzdata/windowsZones.xml
/usr/lib64/R/library/tzdb/tzdata/ziguard.awk
/usr/lib64/R/library/tzdb/tzdata/zishrink.awk
/usr/lib64/R/library/tzdb/tzdata/zone.tab
/usr/lib64/R/library/tzdb/tzdata/zone1970.tab
/usr/lib64/R/library/tzdb/tzdata/zoneinfo2tdf.pl

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/tzdb/libs/tzdb.so
/usr/lib64/R/library/tzdb/libs/tzdb.so.avx2
/usr/lib64/R/library/tzdb/libs/tzdb.so.avx512
