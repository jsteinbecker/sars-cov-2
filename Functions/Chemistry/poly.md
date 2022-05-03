  (Redirected from [Polyglot HTML5](https://en.wikipedia.org/w/index.php?title=Polyglot_HTML5&redirect=no "Polyglot HTML5"))

In computing, a **polyglot markup** is a document or script written in a valid form of multiple [markup languages](https://en.wikipedia.org/wiki/Markup_language "Markup language"), which performs the same output, independent of the markup's [parser](https://en.wikipedia.org/wiki/Parsing "Parsing"), [layout engine](https://en.wikipedia.org/wiki/Browser_engine "Browser engine"), or [interpreter](https://en.wikipedia.org/wiki/Document_Object_Model "Document Object Model"). In general, the _polyglot markup_ is a common subset of two or more languages, that can be used as a robust or simplified profile.

**Polyglot HTML** is [HTML](https://en.wikipedia.org/wiki/HTML "HTML") that has been written to conform to both the HTML and [XHTML](https://en.wikipedia.org/wiki/XHTML "XHTML") specifications.[\[1\]](https://en.wikipedia.org/wiki/Polyglot_markup#cite_note-w3c-1) A polyglot document can therefore be parsed as either HTML (which is [SGML](https://en.wikipedia.org/wiki/SGML "SGML")\-compatible) or [XML](https://en.wikipedia.org/wiki/XML "XML"), and will produce the same [DOM](https://en.wikipedia.org/wiki/Document_Object_Model "Document Object Model") structure either way. For example, in order for an [HTML5](https://en.wikipedia.org/wiki/HTML5 "HTML5") document to meet these criteria, the two requirements are that it must have an HTML5 [doctype](https://en.wikipedia.org/wiki/Document_Type_Declaration "Document Type Declaration"), and be written in well-formed XHTML.[\[2\]](https://en.wikipedia.org/wiki/Polyglot_markup#cite_note-2) The same document can then be served as either HTML or XHTML, depending on browser support and MIME type.

## Polyglot HTML requirements\[[edit](https://en.wikipedia.org/w/index.php?title=Polyglot_markup&action=edit&section=1 "Edit section: Polyglot HTML requirements")\]

As expressed by the _html-polyglot recommendation_,[\[1\]](https://en.wikipedia.org/wiki/Polyglot_markup#cite_note-w3c-1) to write a polyglot HTML5 document, the following key points should be observed:

1.  Processing instructions and the XML declaration are both forbidden in polyglot markup
2.  Specifying a document’s character encoding
3.  The DOCTYPE
4.  Namespaces
5.  Element syntax (i.e. End tags are not optional. Use self-closing tags for void elements.)
6.  Element content
7.  Text (i.e. pre and textarea should not start with newline character)
8.  Attributes (i.e. Values must be quoted)
9.  Named entity references (i.e. Only amp, lt, gt, apos, quot)
10.  Comments (i.e. Use <!-- syntax -->)
11.  Scripting and styling polyglot markup

The most basic possible polyglot markup document would therefore look like this:[\[1\]](https://en.wikipedia.org/wiki/Polyglot_markup#cite_note-w3c-1)

```html
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="" xml:lang="">
  <head>
    <title>The title element must not be empty.</title>
  </head>
  <body>
  </body>
</html>

```

In a polyglot markup document non-void elements (such as `script`, `p`, `div`) cannot be self-closing even if they are empty, as this is not valid HTML.[\[3\]](https://en.wikipedia.org/wiki/Polyglot_markup#cite_note-3) For example, to add an empty textarea to a page, one cannot use `<textarea/>`, but has to use `<textarea></textarea>` instead.

## See also\[[edit](https://en.wikipedia.org/w/index.php?title=Polyglot_markup&action=edit&section=2 "Edit section: See also")\]

-   [Polyglot (computing)](https://en.wikipedia.org/wiki/Polyglot_(computing) "Polyglot (computing)")

## References\[[edit](https://en.wikipedia.org/w/index.php?title=Polyglot_markup&action=edit&section=3 "Edit section: References")\]

1.  ^ [Jump up to: _**a**_](https://en.wikipedia.org/wiki/Polyglot_markup#cite_ref-w3c_1-0) [_**b**_](https://en.wikipedia.org/wiki/Polyglot_markup#cite_ref-w3c_1-1) [_**c**_](https://en.wikipedia.org/wiki/Polyglot_markup#cite_ref-w3c_1-2) [Polyglot Markup: A robust profile of the HTML5 vocabulary](https://www.w3.org/TR/html-polyglot/), W3C Working Group Note 29 September 2015
2.  **[^](https://en.wikipedia.org/wiki/Polyglot_markup#cite_ref-2 "Jump up")** [The WhatWG Blog - XHTML5 in a nutshell](https://blog.whatwg.org/xhtml5-in-a-nutshell), 25 July 2010
3.  **[^](https://en.wikipedia.org/wiki/Polyglot_markup#cite_ref-3 "Jump up")** [Polyglot Markup: HTML-Compatible XHTML Documents: 6.4 Void Elements](http://dev.w3.org/html5/html-xhtml-author-guide/html-xhtml-authoring-guide.html#empty-elements). W3C Editor's Draft 9 July 2012.

## External links\[[edit](https://en.wikipedia.org/w/index.php?title=Polyglot_markup&action=edit&section=4 "Edit section: External links")\]

-   [https://en.wikibooks.org/wiki/Polyglot\_markup,\_how\_to](https://en.wikibooks.org/wiki/Polyglot_markup,_how_to)
-   [CSE HTML Validator for Windows with polyglot markup support](https://www.htmlvalidator.com/)
-   [Benefits of polyglot XHTML5](http://www.xmlplease.com/xhtml/xhtml5polyglot/)