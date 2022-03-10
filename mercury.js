import Mercury from '@postlight/mercury-parser';

Mercury.parse(url).then(result => console.log(result));

// NOTE: When used in the browser, you can omit the URL argument
// and simply run `Mercury.parse()` to parse the current page.