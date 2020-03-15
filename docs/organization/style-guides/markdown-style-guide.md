---
layout: handbook-page-toc
title: Markdown Guide
description: Read through how we style our markdown documents
---

# Markdown Style Guide

If you never have written a single line in markdown markup, don't worry, it's easy to learn and even easier to use. You'll probably be surprised how handy it is once you get used to it. And you'll miss it whenever the tech you're using doesn't support markdown.

This guide has been made to make it easier for everyone to use kramdown features and save a lot of time writing content for various pages on Bit Project's website including handbook pages, website pages, blog posts and everything else. 

There are different possible syntaxes for most of the markups described below, but this guide is to be considered the standard for Bit Project.

## Headings

```text
## Heading h2

### Heading h3

#### Heading h4
```

{::options parse\_block\_html="true" /}

 \*\*Output\*\* {: .panel-heading} \#\# Heading h2 {:.no\_toc style="margin-top:0"} \#\#\# Heading h3 {:.no\_toc} \#\#\#\# Heading h4 {:.no\_toc}

Notes:

* We don't use `h1` headings, as they already are displayed on every page as its title, and we should not apply more than one `h1` per page.

  > _When you use a top level heading, or an , you’re setting up a semantic relationship between that heading and the remainder of the content on a page, describing what it is about. If you then use a second  on the same page, you’re creating some potential confusion, because someone, or a search engine might see that as the ending of the semantic relationship between the content after the first  and the start of this new ._ [SEO Guide](http://www.seobythesea.com/2012/01/heading-elements-and-the-folly-of-seo-expert-ranking-lists/)

* Always start with `h2` \(`##`\), and respect the order h2 → h3 → h4. Never skip the hierarchy level, such as h2 → h4.

  > _The six heading elements, H1 through H6, denote section headings. Although the order and occurrence of headings is not constrained by the HTML DTD, documents **should not skip levels** \(for example, from H1 to H3\), as converting such documents to other representations is often problematic._ [W3C](https://www.w3.org/MarkUp/html-spec/html-spec_5.html#SEC5.4)

* Always leave a blank space between the hash `#` and the text next to it, otherwise it won't render properly.
* For keeping the text clear and the markdown consistent, [jump a line]() between any heading and its subsequent paragraph.

## Paragraphs, breaks, and horizontal lines

Regular paragraphs are obtained by just writing text lines. If you hit **enter** between two lines, both lines will be joined into a single paragraph, which is called [wrapping text](/2016/10/11/wrapping-text/#do-wrap-it). But, if you leave a blank line between them, they will split into two paragraphs.

It is a best practice to write each a paragraph on a single line. Don't put line breaks at the end of each sentence, and don't break up lines at a certain character limit. It is very difficult to review and edit copy with artificial lines breaks.

In some Git tools, `diffs` in future MRs may be easier to understand with additional line breaks, however GitLab's web interface as well as many desktop Git tools feature substring change highlighting within lines and side-by-side or similar version comparison so there is no need for artificial line breaks.

### Wrapping Text

We usually break the lines within paragraphs to facilitate reviews. Do not leave blank spaces after the last word of the line broken within a paragraph, unless you want it to be intentionally broken with a `<br>`.

#### Regular paragraphs and automatic join

```text
This text is a paragraph.
This won't be another paragraph, it will join the line above it.

This will be another paragraph, as it has a blank line above it.
```

 \*\*Output\*\* {: .panel-heading} This text is a paragraph. This won't be another paragraph, it will join the line above it. This will be another paragraph, as it has a blank line above it.

### Additional breaks

In case you need an additional break \(or some extra space between lines\), you can simply use the HTML break tag `<br>`, leaving blank lines above and below it:

```markup
Text A
<!-- blank line -->
<br>
<!-- blank line -->
Text B
```

 \*\*Output\*\* {: .panel-heading} Text A  
 Text B

### Horizontal lines

A sequence of three or more dashes will produce a horizontal line, but let's use always **4** as standard. Leave blank lines after and before it:

```markup
Text
<!-- blank line -->
----
<!-- blank line -->
Text
```

 \*\*Output\*\* {: .panel-heading} Text ---- Text

## Emphasis: bold and italic

To display bold or italic text, wrap it in stars or underlines:

```text
This is **bold** and this is _italic_.
```

 \*\*Output\*\* {: .panel-heading} This is \*\*bold\*\* and this is \_italic\_.

## Links

There are a few different ways to display links with markdown markup, but to keep some standards, let's try to use the following options only.

Important notes: {: \#links-important-notes}

* {: \#note-meaningful-links} Don't take it as a restrictive rule, but [avoid using meaningless text for links](/handbook/communication/#writing-style-guidelines) as "this article"

  or "read here." The link text should be meaningful even if taken out of context; this makes the links more useful and accessible for people using screen readers.

* {: \#note-deadlinks-checker} Check for broken links: [http://www.deadlinkchecker.com/](http://www.deadlinkchecker.com/)

### Inline Links

We'd rather use inline links, such as `[Text to display](link)`, as they are easier to maintain.

### Relative links

Use relative links when referring to links found on [about.gitlab.com](/). For example, a link to our blog handbook should look like this `/handbook/marketing/blog/` and **not** this `https://about.gitlab.com/handbook/marketing/blog/`. Remove everything from the `https` through `about.gitlab.com`, but retain the forward slash after `.com`.

For links to GitLab.com or anywhere else you must use the entire link, including the `http:`.

### Mailto links

If you're adding an email address to a page be sure to format your link with `mailto` to avoid creating broken links. For example, `[example@gitlab.com](mailto:example@gitlab.com)`

### Identifiers

When there are **repeated** links across a single page, you can opt for using identifiers.

Place the identifiers at the end of the paragraph \(or the section\), arranging them in alphabetical order.

```text
[Text to display][identifier] will display a link.

[Another text][another-identifier] will do the same. Hover the mouse over it to see the title.

[This link] will do the same as well. It works as the identifier itself.

[This link][] (same as above), has a second pair of empty brackets to indicate that the following parenthesis does not contain a link.

<https://example.com> works too. Must be used for explicit links.

<!-- Identifiers, in alphabetical order -->
```

 \*\*Output\*\* {: .panel-heading} \[Text to display\]\[identifier\] will display a link. \[Another text\]\[another-identifier\] will do the same. Hover the mouse over it to see the title. \[This link\] will do the same as well. It works as the identifier itself. \[This link\]\[\] \(same as above\), has a second pair of empty brackets to indicate that the following parenthesis does not contain a link. works too. Must be used for explicit links.

Note:

* {: \#note-identifiers} Identifiers **are not** case sensitive. They can be single words as `[link]` or `[multiple words too]`.

## Lists

Both ordered and unordered lists are very straight-forward to produce. There are a few ways to produce the same results, but let's stick with the following, again, to maintain some standards.

Always use **3** blank spaces to indent a nested list \(to create sub items\).

Tip: don't leave blank lines **between the items**, unless you have a reason to do so.

**Important:** always leave a blank line between the paragraph or heading and the subsequent list! If you don't, the list will not render. {:.alert .alert-info}

### Ordered lists

Ordered lists are pretty easy to create. Couldn't be more intuitive:

```text
Paragraph:

1. Item one
   1. Sub item one
   2. Sub item two
   3. Sub item three
2. Item two
```

 \*\*Output\*\* {: .panel-heading} Paragraph: 1. Item one 1. Sub item one 2. Sub item two 3. Sub item three 2. Item two

To be practical and avoid errors on the numbers, use "1" for all the items. The markdown engine will output them in the correct order.

```text
Paragraph:

1. Item one
   1. Sub item one
   1. Sub item two
1. Item two
1. Item three
```

 \*\*Output\*\* {: .panel-heading} Paragraph: 1. Item one 1. Sub item one 2. Sub item two 1. Item two 1. Item three

### Unordered lists

Unordered lists are very easy to create too:

```text
Paragraph:

- Item 1
- Item 2
- Item 3
   - Sub item 1
   - Sub item 2
- Item 4
```

 \*\*Output\*\* {: .panel-heading} Paragraph: - Item 1 - Item 2 - Item 3 - Sub item 1 - Sub item 2 - Item 4

### Split lists

Let's say, for some reason, you want to split a list in different parts. To do that, use the markup `^` to indicate the end of a list and the beginning of the next:

```text
- list one - item 1
- list one - item 2
   - sub item 1
   - sub item 2
- list one - item 3
^
- list two - item A
- list two - item B
^
- list three - item _i_
- list three - item _ii_
```

 \*\*Output\*\* {: .panel-heading} - list one - item 1 - list one - item 2 - sub item 1 - sub item 2 - list one - item 3 ^ - list two - item A - list two - item B ^ - list three - item \_i\_ - list three - item \_ii\_

## Images

To insert images to your markdown file, use the markup `![ALT](/path/image.ext)`. The path can either be relative to the website, or a full URL for an external image. The supported formats are `.png`, `.jpg`, `.gif`. You might be able to use some `.svg` files too, depending on its structure.

```text
![Semantic description of image](/images/path/to/folder/image.png "Image Title")
```

You can also use an identifier, as we do for [links]():

```text
![Semantic description of image][identifier]
```

If you want to add a caption to your image, it's easily achieved with:

```text
![Semantic description of image](/images/path/to/folder/image.png)*My caption*
```

For clickable images, simply wrap the image markup into a [link markup]():

```text
[![Semantic description of image](/images/path/to/folder/image.png "Hello World")*My caption*][about.gitlab.com]
```

 \*\*Output\*\* {: .panel-heading} \[!\[Semantic description of image\]\(/images/about-gitlab-com.png "Hello World"\)\*My caption\*\]\[about.gitlab.com\]

**Important notes:** {:\#images-important-notes}

* {: \#image-shadow} Apply [shadow]() to your images!
* {: \#image-requirements} All images must be placed [under `/source/images/`](https://gitlab.com/gitlab-com/www-gitlab-com/tree/master/source/images), in an appropriate directory. Only screenshots

  and public domain images are permitted.

* {: \#image-alt-text} The text inside the square brackets is an image attribute called `ALT`, which stands for _alternative text_.

  [Including descriptive alt text](https://webaim.org/techniques/alttext/) helps maintain accessibility for every visitor and should always be included with an image. When you add alt text be sure to describe the content and function of an image. In addition to the accessibility benefits, `ALT` is useful for SEO, and it is displayed when, for some reason, that image is not loaded by the browser.

* {: \#image-filename} For the same reasons, the image must contain a name related to it. Example: instead of `image-01.jpg`,

  name it `black-dog.jpg`, if it's a photo of a black dog.

* {: \#image-title} It's also recommendable adding an image title, as the "Hello World" exemplified above.

## Diagrams



## Videos

There are two ways of displaying videos: within HTML5 `<video>` tags and within `<iframe>` tags.

### Display videos from YouTube

This method works for YouTube videos and any other embed video within an `<iframe>` tag.

1. Copy the code below and paste it into your markdown file. Leave a blank line above

   and below it. **Do NOT edit the code block** \(e.g., remove spaces - the video iframe

   may not render properly\)

2. Go the video URL you want to display
3. Click on "Share", then "Embed"
4. Copy the `<iframe>` source \(`src`\) URL **only**, and paste it replacing the `src` below:

```markup
<!-- blank line -->
<figure class="video_container">
  <iframe src="https://www.youtube.com/embed/enMumwvLAug" frameborder="0" allowfullscreen="true"> </iframe>
</figure>
<!-- blank line -->
```

 \*\*Output\*\* {: .panel-heading}

### Display local videos \(HTML5\)

This method works for any video uploaded to somewhere retrievable from the internet from a URL, or from a relative path like `path/to/video.mp4`.

1. Read through the [w3schools HTML5 video guide](http://www.w3schools.com/tags/tag_video.asp), or the [MDN `<video>` guide](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/video).
2. Record or export the video in these three formats to achieve cross-browser and cross-device

   compatibility: `.mp4`, `.ogg` and `.webm`.

3. Get the URL for your video
4. Choose an image to use as a poster
5. Copy the code below and paste it to your file
6. Replace the `src` URLs for your video URLs

```markup
<!-- blank line -->
<figure class="video_container">
  <video controls="true" allowfullscreen="true" poster="path/to/poster_image.png">
    <source src="path/to/video.mp4" type="video/mp4">
    <source src="path/to/video.ogg" type="video/ogg">
    <source src="path/to/video.webm" type="video/webm">
  </video>
</figure>
<!-- blank line -->
```

 \*\*Output\*\* {: .panel-heading}

_**Note:** in case you don't have all formats recommended by **w3schools**, you can use just one of them, but your video most likely won't be supported in all devices and browsers. The video above \(`.mp4` only\) worked on Mozilla Firefox for OS X, Android, and Windows, and on Chrome for Android and for Windows. But it may not work on other devices/browser, such as Chrome for OS X and iOS, or Safari. In fact, the best option is using YouTube or Vimeo embed videos in `<iframe>` tags._ {: .note}

### Display other videos

For any other videos, such as from Vimeo or Google Drive, grab the video iframe only, and proceed like we do for [YouTube videos](), wrapping the `<iframe>` within a `<figure class="video_container">`, for responsiveness. Copy and paste the code below, replacing **only** the iframe URL with your own:

```markup
<!-- blank line -->
<figure class="video_container">
  <iframe src="https://drive.google.com/file/d/0B6m34D8cFdpMZndKTlBRU0tmczg/preview" frameborder="0" allowfullscreen="true"> </iframe>
</figure>
<!-- blank line -->
```

 \*\*Output\*\* {: .panel-heading}

### Display multiple videos

To display multiple videos on the same page, just repeat the `figure` code block where you want them to show up, replacing the video ID with the respective ID corresponding to your videos.

To display multiple videos in a sequence, just copy the `figure` code block and paste it as many times as necessary. Always leave a blank line between the blocks. Do **NOT** remove the spaces, otherwise your videos may not render properly.

```markup
<!-- blank line -->
<figure class="video_container">
  <iframe src="https://drive.google.com/file/d/0B6m34D8cFdpMZndKTlBRU0tmczg/preview" frameborder="0" allowfullscreen="true"> </iframe>
</figure>

<figure class="video_container">
  <iframe src="https://drive.google.com/file/d/0B6m34D8cFdpMZndKTlBRU0tmczg/preview" frameborder="0" allowfullscreen="true"> </iframe>
</figure>

<figure class="video_container">
  <iframe src="https://drive.google.com/file/d/0B6m34D8cFdpMZndKTlBRU0tmczg/preview" frameborder="0" allowfullscreen="true"> </iframe>
</figure>
<!-- blank line -->
```

## Table of Contents \(ToC\)

With kramdown, creating a Table of Contents is the easiest thing ever! The automatic ToC will include every heading in the document, unless you don't want it to be included. You do not need to add anchors individually to every title. This is an automated process.

```text
----

## On this page
{:.no_toc}

- TOC
{:toc}

----
```

As always, leave a blank line before and after the markup. Note that there are four dashes beginning and closing the block, which is not required, but recommendable for keeping the same standards throughout [about.GitLab.com](/).

The heading "On this page" can be adapted to your case, e.g., "In this tutorial", or "In this guide", etc. It's not required either, but recommended.

The markup `{:.no_toc}` is used every time you don't want to include a heading into the ToC. Just add it right below the heading, and it won't be included into the ToC. In fact `no_toc` is a [custom class](), as described later in this guide.

The **output** ToC can be found at the very beginning of this page.

Alternatively, you can use ordered ToC too, displaying numbers at the beginning of the list. Just use the markup for ordered lists and kramdown will be smart enough to understand what you want:

```text
1. TOC
{:toc}
```

## Tables

Tables for markdown are challenging. So, we have two possible approaches: use markdown whenever possible, but if you need pretty advanced table layouts, you are free to add them in HTML markup instead.

> _Markdown is not a replacement for HTML, or even close to it. \(_[_John Gruber_](http://daringfireball.net/projects/markdown/syntax#html)_\)_ {: \#quote}

As explained by John Gruber, the creator of markdown, it was not created to replace HTML, so there are situations we can't avoid using HTML. With complex tables, that's the case.

The following table has a header \(first line\), then markup to define the desired alignment \(dashes and colons\), then the table body. You can go ahead and add separators to create subsequent table bodies.

However you prepare your table, its design will depend upon the CSS styles defined for them.

The last markup `{: .custom-class #custom-id}` **can** be used in case you want to attribute a [custom class and/or a custom ID]() to the `<table>` element.

```text
| Default aligned | Left aligned | Center aligned  | Right aligned  |
|-----------------|:-------------|:---------------:|---------------:|
| First body part | Second cell  | Third cell      | fourth cell    |
| Second line     | foo          | **strong**      | baz            |
| Third line      | quux         | baz             | bar            |
|-----------------+--------------+-----------------+----------------|
| Second body     |              |                 |                |
| 2nd line        |              |                 |                |
|-----------------+--------------+-----------------+----------------|
| Third body      |              |                 | Foo            |
{: .custom-class #custom-id}
```

 \*\*Output\*\* {: .panel-heading} \| Default aligned \| Left aligned \| Center aligned \| Right aligned \| \|-----------------\|:-------------\|:---------------:\|---------------:\| \| First body part \| Second cell \| Third cell \| fourth cell \| \| Second line \| foo \| \*\*strong\*\* \| baz \| \| Third line \| quux \| baz \| bar \| \|-----------------+--------------+-----------------+----------------\| \| Second body \| \| \| \| \| 2nd line \| \| Hello World \| \| \|-----------------+--------------+-----------------+----------------\| \| Third body \| \| \| Foo \| {: .custom-class \#custom-id}

Certain tools can help you to create your own complex table if you need merging lines or columns, and more advanced layouts. This is a [Table Generator](http://www.tablesgenerator.com/html_tables) that might help you out.

Note that the bars, spaces, and dashes were used symmetrically above just for providing a nice view of the table markup. The symmetry is not required.

Read through the [kramdown syntax guide](http://kramdown.gettalong.org/syntax.html#tables) on tables for further information.

## Code blocks

There are a few options for displaying code blocks with kramdown. Most of them use backticks ````` .

### In-line

This is an ```in-line```  code block.

 \*\*Output\*\* {: .panel-heading} \_In-line\_ This is an \`in-line\` code block.

### Fenced

```text
    def hello
       puts "Hello world!"
    end
```

_Fenced Highlighted_

```ruby
    def hello
       puts "Hello world!"
    end
```

or

```text
    def hello
       puts "Hello world!"
    end
```

```text
{: .language-ruby}
```

 \*\*Output\*\* {: .panel-heading} \_Fenced\_ \`\`\` def hello puts "Hello world!" end \`\`\` \_Fenced Highlighted\_ \`\`\`ruby def hello puts "Hello world!" end \`\`\` or \`\`\` def hello puts "Hello world!" end \`\`\` {: .language-ruby}

### Indented

Add 4 white spaces before every line:

```text
    def hello
       puts "Hello world!"
    end
```

_Indented Highlighted_

```text
    def hello
       puts "Hello world!"
    end
{: .language-ruby}
```

 \*\*Output\*\* {: .panel-heading} \_Indented\_ def hello puts "Hello world!" end \_Indented Highlighted\_ def hello puts "Hello world!" end {: .language-ruby}

### Nested

Add 4 white spaces before every line. This is used when you want to display a code block within a code block.

```text
        def hello
           puts "Hello world!"
        end
```

 \*\*Output\*\* {: .panel-heading} \_Nested\_ \`\`\` def hello puts "Hello world!" end \`\`\`

### In lists

Indent the text of each item in 3 white spaces. Leave blank lines between the code block and the list items, and ident the code block in 5 white spaces:

1. Item 1
2. Item 2

   ```ruby
   def hello
      puts "Hello world!"
   end
   ```

3. Item 3

 \*\*Output\*\* {: .panel-heading} 1. Item 1 1. Item 2 \`\`\`ruby def hello puts "Hello world!" end \`\`\` 1. Item 3

## Blockquotes

Blockquotes are good resources to mentioning someone else's quotes, like we did [just above](). Also, can be used to emphasize a sentence or a small paragraph.

```text
> This is a blockquote.
>     On multiple lines.
That may be lazy.
>
> This is the second paragraph.

----

> This is a paragraph.
>
> > A nested blockquote.
>
> ### Headers work
>
> * lists too
>
> and all other block-level **elements**.
>
> Even code blocks:
>
>      def hello
>        puts "Hello world!"
>      end
> {: .language-ruby}
```

 \*\*Output\*\* {: .panel-heading} &gt; This is a blockquote. &gt; On multiple lines. That may be lazy. &gt; &gt; This is the second paragraph. ---- &gt; This is a paragraph. &gt; &gt; &gt; A nested blockquote. &gt; &gt; \#\#\# Headers work &gt; {:.no\_toc} &gt; &gt; \* lists too &gt; &gt; and all other block-level \*\*elements\*\*. &gt; &gt; Even a code block: &gt; &gt; def hello &gt; puts "Hello world!" &gt; end &gt; {: .language-ruby}

## Notes

```text
This is a regular paragraph.

**Note:** a note is something that needs to be mentioned but is apart from the context.
{: .note}
```

 \*\*Output\*\* {: .panel-heading} This is a regular paragraph. \*\*Note:\*\* a note is something that needs to be mentioned but is apart from the context. {: .note}

## Comments

_Markdown markup_

```text
This is a paragraph
{::comment}
This is a comment which is
completely ignored.
{:/comment}
... paragraph continues here.
```

_Regular HTML markup_

{: .language-html}

 \*\*Output\*\* {: .panel-heading} This is a paragraph {::comment} This is a comment which is completely ignored. {:/comment} ... paragraph continues here.

## Anchors

Add an anchor anywhere with:

```text
[](){: name="hello-world"}

Some text
```

Or simply use an ID:

```text
Some text
{: #hello-world}
```

## Font Awesome

Yes, we can use fancy [Font Awesome](http://fontawesome.io/icons/) icons too.

_Regular_

```text
### <i class="fas fa-puzzle-piece" aria-hidden="true"></i> Puzzle Icon
{: #puzzle}
```

And you can go further, such as the following.

_Styled_

```text
### <i class="fab fa-gitlab fa-fw" style="color:rgb(107,79,187); font-size:.85em" aria-hidden="true"></i> Purple GitLab Tanuki
{: #tanuki-purple}

### <i class="fab fa-gitlab fa-fw" style="color:rgb(252,109,38); font-size:.85em" aria-hidden="true"></i> Orange GitLab Tanuki
{: #tanuki-orange}
```

 \*\*Output\*\* {: .panel-heading} \_Regular\_ \#\#\# Puzzle Icon {: \#puzzle} ---- \_Styled\_ \#\#\# Purple GitLab Tanuki {: \#tanuki-purple} \#\#\# Orange GitLab Tanuki {: \#tanuki-orange}

When doing something like this to a heading, it's important give it a custom ID \(e.g., `{: #puzzle}`\), otherwise the one automatically created by kramdown will sound very awkward.

The class `fa-fw` is used when you want to display the icons as a list. They will be aligned, as well as the text right beside them.

See live examples [on this post](/2016/06/10/ssg-overview-gitlab-pages-part-2/), where the icons are used to illustrate the text.

## Classes, IDs, and attributes

Defining CSS classes, and elements IDs and attributes with markdown is definitely something unusual \(kramdown magic!\).

But yes, if you know how to use it, you'll love it! Check how easy it is to do that with kramdown:

```text
Paragraph
{: .class .class-1 .class-2}

Paragraph
{: #custom-id}

Paragraph
{: .class .class-1 #custom-id-1}

## Heading
{: .class .class-1 #custom-id-2}

Paragraph
{: .class #custom-id-3 style="padding-top:0" key="value"}

## Heading {#hello}

List:

- {: .class} List item with custom class
- {:#id} List item with custom id

To a [link]{: #link}, in-line.

This is a [link][google-es]{:hreflang="es"} in Spanish.
```

 \*\*Output\*\* {: .panel-heading} Paragraph {: .class .class-1 .class-2} Paragraph {: \#custom-id} Paragraph {: .class .class-1 \#custom-id-1} \#\#\# Heading {: .class .class-1 .no\_toc \#custom-id-2} Paragraph {: .class \#custom-id-3 style="padding-top:0" key="value"} \#\#\# Heading {\#hello} {: .no\_toc} List: - {: .class} List item with custom class - {:\#id} List item with custom id To a \[link\]{: \#link}, in-line. This is a \[link\]\[google-es\]{:hreflang="es"} in Spanish.

### Special classes

#### Shadow

The CSS class called `shadow` should be used when your image edges are not clearly defined. This happens when it has a white background or when it's a screenshot with text \(for example, a screenshot of our user interface\). For example, this image can be mistaken as part of the text:

Now, if you apply the class `shadow` to the image, it's discreetly highlighted from the text:

{: .shadow}

To do that, apply the class directly to the image by adding the markup `{: .shadow}` right after the image markup:

```text
![image alternative text](/path/to/image.png){: .shadow}
```

#### Note

As [previously]() explained, you can add the class `note` to paragraphs that you don't want to call attention to:

**Note:** this is something I don't want to call attention to. {: .note}

Markup:

```text
**Note:** this is something I don't want to call attention to.
{: .note}
```

#### Colors

Add a custom class to a heading or paragraph using the following special classes.

**GitLab Orange**

#### GitLab Orange Heading

{:.gitlab-orange .no\_toc}

Markup:

```text
### GitLab Orange Heading
{: .gitlab-orange}
```

**GitLab Purple**

#### GitLab Purple Heading

{:.gitlab-purple .no\_toc}

Markup:

```text
### GitLab Purple Heading
{: .gitlab-purple}
```

#### Text Align

By default, the text will always be aligned to the left. You have a few options to customize it with custom classes:

* Center: `.text-center`
* Right: `.text-right`
* Justify: `.text-justify`

For demonstrations purposes, they are aligned in an [alert box](), but this can be applied to regular paragraphs and headings.

**Align to the center**

Center-aligned {: .alert .alert-info .text-center}

Alert box markup:

```text
Center-aligned
{: .alert .alert-info .text-center}
```

Paragraph markup:

```text
Center-aligned
{: .text-center}
```

Heading markup:

```text
### Center-aligned
{: .text-center}
```

**Align to the right**

Right-aligned {: .alert .alert-info .text-right}

```text
Right-aligned
{: .alert .alert-info .text-right}
```

**Justify**

Justified {: .alert .alert-info .text-justify}

```text
Justified
{: .alert .alert-info .text-justify}
```

## Mix HTML + Markdown Markup

Mixing HTML markup with markdown is something almost "unthinkable" to someone used to regular markdown. And it's all over this document!

Use the following markup at the beginning of your document:

```text
{::options parse_block_html="true" /}
```

And feel free to mix everything up:

```text
Something in **markdown**.

<p>Then an HTML tag with crazy **markup** _all over_ the place!</p>
```

 \*\*Output\*\* {: .panel-heading} Something in \*\*markdown\*\*.

Then an HTML tag with crazy \*\*markup\*\* \_all over\_ the place!

You can close the markup parser tag at any point, if you want to:

```text
{::options parse_block_html="false" /}
```

## Colorful sections

To add notes and warning blocks into colorful boxes, we are making use of Bootstrap's [panel blocks](https://getbootstrap.com/components/#panels-alternatives) and [alert boxes](https://getbootstrap.com/components/#alerts).

Colorful sections are applied for very specific purposes and must not be overused.

Use panels when your description contains more than one paragraph, or a long paragraph. For single and short paragraphs, use alert boxes instead.

When using panels, make sure to add the HTML parser markup to the beginning of your document's body: `{::options parse_block_html="true" /}`. {: \#html-parser}

Copy paste the following code according to what you want to present to the user and replace only the description. The available colors are: blue \(`info`\), green \(`success`\), amber \(`warning`\) and red \(`danger`\), as follows.

### Additional Information

Use the following code for **important notes** and additional information:

```markup
<div class="panel panel-info">
**Note**
{: .panel-heading}
<div class="panel-body">

NOTE DESCRIPTION

</div>
</div>
```

To apply to a single paragraph, use an alert box:

```text
My important paragraph.
{: .alert .alert-info}
```

Blue panels render like:

 \*\*Note\*\* {: .panel-heading} NOTE DESCRIPTION

And blue alert boxes render like:

My important paragraph. {: .alert .alert-info}

If you want the text inside the alert box to be blue as well, we need to apply [custom styles]() to the markdown document. They will override the existing ones. Add the following `style` tag to the end of your file.

```css
<style>
.alert-info {
  color: rgb(49,112,143) !important;
}
</style>
```

### Warnings

Use the following code for warnings, like information that may have a different result if not used correctly:

```markup
<div class="panel panel-warning">
**Warning**
{: .panel-heading}
<div class="panel-body">

WARNING DESCRIPTION

</div>
</div>
```

To apply to a single paragraph, use an alert box:

```text
My warning paragraph.
{: .alert .alert-warning}
```

Amber panels render like:

 \*\*Warning\*\* {: .panel-heading} WARNING DESCRIPTION

And amber alert boxes render like:

My warning paragraph. {: .alert .alert-warning}

If you want the text inside the alert box to be amber as well, we need to apply [custom styles]() to the markdown document. They will override the existing ones. Add the following `style` tag to the end of your file.

```css
<style>
.alert-warning {
  color: rgb(138,109,59) !important;
}
</style>
```

### Danger

Use the following code for crucial warnings, like commands that result in loss of data:

```markup
<div class="panel panel-danger">
**Danger**
{: .panel-heading}
<div class="panel-body">

DANGER DESCRIPTION

</div>
</div>
```

To apply to a single paragraph, use an alert box:

```text
My danger paragraph.
{: .alert .alert-danger}
```

Red panels render like:

 \*\*Danger\*\* {: .panel-heading} DANGER DESCRIPTION

And red alert boxes render like:

My danger paragraph. {: .alert .alert-danger}

If you want the text inside the alert box to be red as well, we need to apply [custom styles]() to the markdown document. They will override the existing ones. Add the following `style` tag to the end of your file.

```css
<style>
.alert-danger {
  color: rgb(169,68,66) !important;
}
</style>
```

### Do's and Don'ts

You can use the combination of green and red panels or alert boxes for "Do's and Don'ts":

```markup
<div class="panel panel-success">
**Do's**
{: .panel-heading}
<div class="panel-body">

THINGS TO DO

</div>
</div>
```

or, use an alert box:

```text
TO DO.
{: .alert .alert-success}
```

Not to do:

```markup
<div class="panel panel-danger">
**Don'ts**
{: .panel-heading}
<div class="panel-body">

THINGS NOT TO DO

</div>
</div>
```

or, use an alert box:

```text
NOT TO DO.
{: .alert .alert-danger}
```

By doing so, the green panels for "DO'S" will look like:

 \*\*Do's\*\* {: .panel-heading} THINGS TO DO

or, if you chose an alert box:

TO DO. {: .alert .alert-success}

If you want the text inside the alert box to be green as well, we need to apply [custom styles]() to the markdown document. They will override the existing ones. Add the following `style` tag to the end of your file.

```css
<style>
.alert-green {
  color: rgb(60,118,61) !important;
}
</style>
```

And for your "DON'TS" within red panels will look like:

 \*\*Don'ts\*\* {: .panel-heading} THINGS NOT TO DO

or, if you chose a red alert box:

NOT TO DO. {: .alert .alert-danger}

### Custom alert panels and alert boxes

All the previously mentioned alert boxes and panels are available by default by [Bootstrap](http://getbootstrap.com/components/#alerts). If we want them in a different color, we need [custom styles](). At [about.GitLab.com](/), we can use the orange and the purple one, as follows.

When using panels, don't forget to add to the beginning of your file the [HTML parser markup]() to be able to mix HMTL + Markdown: `{::options parse_block_html="true" /}`.

#### GitLab Orange Alert Panel

 \*\*Heading\*\* {: .panel-heading} Text in markdown.

Panel block markup:

```markup
<div class="panel panel-gitlab-orange">
**Heading**
{: .panel-heading}
<div class="panel-body">

Text in markdown.

</div>
</div>
```

#### GitLab Orange Alert Box

My text in an orange box. {: .alert .alert-gitlab-orange}

Box block markup:

```text
My text in an orange box.
{: .alert .alert-gitlab-orange}
```

#### GitLab Purple Alert Panel

 \*\*Heading\*\* {: .panel-heading} Text in markdown.

Panel block markup:

```markup
<div class="panel panel-gitlab-purple">
**Heading**
{: .panel-heading}
<div class="panel-body">

Text in markdown.

</div>
</div>
```

#### GitLab Purple Alert Box

My text in an purple box. {: .alert .alert-gitlab-purple}

Box block markup:

```text
My text in an purple box.
{: .alert .alert-gitlab-purple}
```

### GitLab Webcast Alert Box

To be used in a CTA for webcast announcement in blog posts. You can use it for other purposes as well. Use it together with the [HMTL parser]():

   The webcast I want to announce - [Register here]()!    {: .alert .alert-webcast}

```text
{::options parse_block_html="true" /}

<i class="fab fa-gitlab" style="color:rgb(107,79,187); font-size:.85em" aria-hidden="true"></i>&nbsp;&nbsp;
The webcast I want to announce - [Register here][webcast-link]!
&nbsp;&nbsp;<i class="fab fa-gitlab" style="color:rgb(107,79,187); font-size:.85em" aria-hidden="true"></i>
{: .alert .alert-webcast}
```

## Styles

Yes, guess what?

This:

```css
<style>
  .purple {
    color:inherit;
  }
  .purple:hover {
    color:rgb(107,79,187);
  }
</style>
```

  
  .purple {  
    color:inherit;  
  }  
  .purple:hover {  
    color:rgb\(107,79,187\);  
  }  


Plus:

```text
Hey! Hover the cursor over me and guess what?! :)
{: .purple}
```

Equals to:

 \*\*Output\*\* {: .panel-heading} Hey! Hover the cursor over me and guess what?! :\) {: .purple}

And yes, the `<style>` tag is _in_ this very markdown file. Believe it or not!

## Embed documents

It's easy to embed Google Docs, Sheets, Slides, and pretty much everything that provides an iframe to use with. The only thing you need to do is use the following code inside your markdown file and replace the iframe from the document you want to embed:

```markup
<figure class="video_container">
<iframe IFRAME CONTENT></iframe>
</figure>
```

### Google products

For Google products, with your document opened, click **File** -&gt; **Publish to the web**. For example, here's what Google sheets will look like:

Choose **Embed**, check your settings, click on **Publish** and copy the `<iframe>`. Then go to your markdown file and wrap the iframe into a `<figure>` tag with the responsive `video_container` class, as shown [in the beginning]().

#### Google Sheets

Let's exemplify with this [simple spreadsheet](https://docs.google.com/a/gitlab.com/spreadsheets/d/1jAnvYpRmNu8BISIrkYGTLolOTmlCoKLbuHVWzCXJSY4/edit?usp=sharing). Follow the info [above]() to find the iframe:

Copy the code below and paste to your markdown file \(leave a blank line above and below it\). Then replace the `<iframe>` with your own:

```markup
<figure class="video_container">
<iframe src="https://docs.google.com/spreadsheets/d/1jAnvYpRmNu8BISIrkYGTLolOTmlCoKLbuHVWzCXJSY4/pubhtml?widget=true&amp;headers=false"></iframe>
</figure>
```

#### Output:

{: .no\_toc}

#### Google Slides

Let's exemplify with this [GitLab slide deck](https://docs.google.com/presentation/d/1fWjiVgSNMKTHyC6_nWDY5rDhvdm-zEQMQytZysIXAzk/edit?usp=sharing). Follow the steps [above]() to find the iframe:

Copy the code below and paste to your markdown file \(leave a blank line above and below it\). Then replace the `<iframe>` with your own:

```markup
<figure class="video_container">
<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vS_iuMXnp61wlo4amm5nvHr4Ir8VUzisJSBsr7YEL7fKWAiT-9bmehyngtb9TYaFEsFnRokCyIXwsvY/embed?start=false&loop=false&delayms=3000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
</figure>
```

#### Output:

{: .no\_toc}

#### Google Docs

Embedding Google Docs is not a recommended practice. Prefer converting your document content to markdown instead. If you need to embed it anyway, follow the same instructions and the same logic as we presented for Google Sheets and Slides, wrapping the `<iframe>` with a `<figure>` tag:

```markup
<figure class="video_container">
<iframe src="https://docs.google.com/document/d/1mHhOhvvrz7xgUPyn5VWCNuKgew5MRRGZp761B9prPqs/pub?embedded=true"></iframe>
</figure>
```

### SlideShare

To embed from SlideShare, go to the document you want to embed and hit the **Share** button located below the slides. Copy the code under **Embed** and place it inside the `figure` tag.

 Be careful to only include the iframe content and strip anything else. SlideShare will also add some other information in the embed code which you will have to remove, otherwise the markdown page will be broken. {: .alert .alert-warning}

For example, let's say we wanted to include the slides from [Ivan's talk on GitLab Pages](http://www.slideshare.net/creatop/how-to-use-any-static-site-generator-with-gitlab-pages). Copying the embed code and stripping everything else except from the iframe, would result in this:

```markup
<figure>
<iframe src="//www.slideshare.net/slideshow/embed_code/key/EixD8OUMBX65Jy" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe>
</figure>
```

 You can safely omit the `<figure>` tag since SlideShare's widget is already responsive, but we are showing this that way in order to be consistent with the rest of the handbook. {: .alert .alert-info}

#### Output:

{: .no\_toc}

## Embed Tweets

To add tweets to markdown, copy both `<blockquote>` and `<script>` tags from the twitter post and paste it into your file. To make it look much nicer, wrap the script into a `div.center` \(created for this specific purpose\).

**Important:** if you used the [HTML parser]() in your post or page, you'll need to set it to `false` before the `div`. {:.alert .alert-info}

{::options parse\_block\_html="false" /}

Thanks to [@gitlab](https://twitter.com/gitlab) for joining [@RailsGirlsCluj](https://twitter.com/RailsGirlsCluj)! [pic.twitter.com/NOoiqDWKVY](https://t.co/NOoiqDWKVY)— RailsGirlsCluj \(@RailsGirlsCluj\) [October 8, 2016](https://twitter.com/RailsGirlsCluj/status/784847271645028352)

  
 Markup: \`\`\`md {::options parse\_block\_html="false" /}

> Thanks to [@gitlab](https://twitter.com/gitlab) for joining [@RailsGirlsCluj](https://twitter.com/RailsGirlsCluj)! [pic.twitter.com/NOoiqDWKVY](https://t.co/NOoiqDWKVY)— RailsGirlsCluj \(@RailsGirlsCluj\) [October 8, 2016](https://twitter.com/RailsGirlsCluj/status/784847271645028352)

&lt;/div&gt;

```text
For more than one Tweet, copy and paste all the code blocks from Twitter into one `div.center`:

```md
{::options parse_block_html="false" /}

<div class="center">

<!-- first tweet -->
<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="en" dir="ltr">Thanks to <a href="https://twitter.com/gitlab">@gitlab</a> for joining <a href="https://twitter.com/RailsGirlsCluj">@RailsGirlsCluj</a>! <a href="https://t.co/NOoiqDWKVY">pic.twitter.com/NOoiqDWKVY</a></p>&mdash; RailsGirlsCluj (@RailsGirlsCluj) <a href="https://twitter.com/RailsGirlsCluj/status/784847271645028352">October 8, 2016</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

<!-- second tweet -->
<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="en" dir="ltr">Thanks to <a href="https://twitter.com/gitlab">@gitlab</a> for joining <a href="https://twitter.com/RailsGirlsCluj">@RailsGirlsCluj</a>! <a href="https://t.co/NOoiqDWKVY">pic.twitter.com/NOoiqDWKVY</a></p>&mdash; RailsGirlsCluj (@RailsGirlsCluj) <a href="https://twitter.com/RailsGirlsCluj/status/784847271645028352">October 8, 2016</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

</div>
```

## Embed Instagram posts

To embed posts from Instagram, begin by pasting the following code into your file:

```text
{::options parse_block_html="false" /}

<div align="center">
```

Then go to the relevant Instagram post on the web: Go to the post URL if you have it, or you can search for the username on [Instagram.com](https://www.instagram.com/), visit their profile, and then click the post to expand it. Click the more \[...\] button and select "Embed."

Copy the code and paste it below `<div align="center">`.

Add `</div>` after the code you pasted from Instagram.

## Embed GitLab Snippets

To embed [GitLab Snippets](https://docs.gitlab.com/ee/user/snippets.html#embedded-snippets) to a markdown file, copy the embed code from your public snippet and paste it in the file.

Markup:

```markup
<!-- leave a blank line here -->
<script src="https://gitlab.com/gitlab-org/gitlab-ce/snippets/1717978.js"></script>
<!-- leave a blank line here -->
```

Renders:

## Markdown Editors

Please use one of the following code editors to write in markdown, or another **code editor** of your preference.

It is **not** recommend writing your document in a regular text editor, then copy-pasting to markdown, as it most likely will bring some characters with a different encoding \(non UTF-8\), which will cause the markdown to not render correctly.

In case you don't have a choice and need to import a text already written in a text editor, paste it to your markdown file using **command+shift+V** on a Mac, or **control+shift+V** on Windows or Linux. You might minimize the cause of trouble by pasting without format. But yet, is not guaranteed it is going to work, so double check your HTML output.

_Regular Code Editors_

* [Sublime Text 3](https://www.sublimetext.com/3)
* [Atom](https://atom.io/)

_Markdown editors \(type and preview simultaneously\)_

* Markdown editors for Mac: [Mou](http://25.io/mou/), [iA Writer](https://ia.net/writer/)
* In-browser markdown editor: [StackEdit](https://stackedit.io/)

If you're not used to writing markdown, those editors can be helpful. Check a screenshot below of a file being edited on Mou. On your left, there's the markdown markup you're writing, and on your right, a preview of the output. The preview won't be exactly as the final result, but it's a very good approximation, which gives you a good idea on what you're doing while you type.

[StackEdit](https://stackedit.io/) is awesome too, you can work on a markdown file even if you're away from your computer, or out of resources. It works from every major browser and automatically saves your work to Google Drive.

## Complementary Notes

{: \#tips--tricks}

* Words must be separated by one single space only. Do not leave more blank spaces than the necessary,

  they can render differently than expected and can cause other issues.

* Do not leave blank spaces at the end of sentences.
* {:\#jump-a-line} Always leave a blank line between block-level markup elements, except between list items. Example:

  ```text
    ---- (markup for horizontal line)
    <!-- blank line -->
    Paragraph.
    <!-- blank line -->
    Do not leave blank lines within list items:
    <!-- blank line -->
    - Item 1
    - Item 2
    - Item 3
  ```

  {: .language-html}

* As explained [above](), do **not** skip headings. Always do h1 → h2 → h3 → h4. Never h2 → h4.
* Prefer short titles and headings. Do not punctuate them \(unless they require a question mark or an exclamation\).
* Try not to punctuate list items, but if you do, be consistent and do that throughout the list.
* If you have to mention a non-clickable URL, prefer using backticks: `http://an-example.com`.
* To add fancy emojis to your file, click `control+cmd+space` on your Mac and check the ⭐️ **magic** ⭐ or use a website like [Emoji Finder](https://emojifinder.com/). Do not overuse them, please!
* If you are confused about any markup that you've found in this file, you can check its [`raw` file](https://gitlab.com/gitlab-com/www-gitlab-com/raw/master/source/handbook/engineering/ux/technical-writing/markdown-guide/index.html.md) for reference,

  where you'll be able to see exactly how everything was written to produce the results you are seeing on this page.

## More

Anything else you know of and is not described here? Any new magic? Any trick? Please contribute!

