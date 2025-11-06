/* Start a CAS session if not already started */
cas;

/* You can also print CAS options if available */
%put NOTE: CASHOST=%sysfunc(getoption(CASHOST));
%put NOTE: CASPORT=%sysfunc(getoption(CASPORT));
%put NOTE: CASTOKEN=%sysfunc(getoption(ACCESS_TOKEN));




