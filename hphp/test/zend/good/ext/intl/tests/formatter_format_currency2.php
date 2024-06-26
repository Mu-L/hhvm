<?hh

/*
 * Format a number using misc currencies/locales.
 */
/*
 * TODO: doesn't pass on ICU 3.6 because 'ru' and 'uk' locales changed
 * currency formatting.
 */


function ut_main()
:mixed{
    $locales = dict[
        'en_UK' => 'GBP',
        'en_US' => 'USD',
        'ru'    => 'RUR',
        'uk'    => 'UAH',
        'en'    => 'UAH'
    ];

    $res_str = '';
    $number = 1234567.89;

    foreach( $locales as $locale => $currency )
    {
        $fmt = ut_nfmt_create( $locale, NumberFormatter::CURRENCY );
        $res_str .= "$locale: " . var_export( ut_nfmt_format_currency( $fmt, $number, $currency ), true ) . "\n";
    }
    return $res_str;
}

<<__EntryPoint>> function main_entry(): void {
    include_once( 'ut_common.inc' );
    // Run the test
    ut_run();
}
