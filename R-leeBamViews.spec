%bcond_with internet
%global packname  leeBamViews
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.99.13
Release:          1
Summary:          leeBamViews -- multiple yeast RNAseq samples excerpted from Lee 2009
Group:            Sciences/Mathematics
License:          Artistic 2.0
URL:              None
Source0:          http://bioconductor.org/packages/data/experiment/src/contrib/leeBamViews_0.99.13.tar.gz
Requires:         R-Biobase R-Rsamtools R-BSgenome
Requires:         R-GenomicRanges R-methods
Requires:         R-GenomeGraphs R-biomaRt R-org.Sc.sgd.db R-edgeR
BuildRequires:    R-devel Rmath-devel texlive-collection-latex
BuildRequires:    R-Biobase R-Rsamtools R-BSgenome
BuildRequires:    R-GenomicRanges R-methods
BuildRequires:    R-GenomeGraphs R-biomaRt R-org.Sc.sgd.db R-edgeR

%description
data from PMID 19096707; prototype for managing multiple NGS samples

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%if %{with internet}
%check
%{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/bam
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
