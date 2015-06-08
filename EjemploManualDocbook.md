
```
<?xml version="1.0" encoding="UTF-8"?>
<article>
  <title>Amara XML Toolkit manual (for version 1.2)</title>
  <subtitle>User Manual</subtitle>
  <articleinfo>
    <abstract>
      <para/>
    </abstract>

    <revhistory>
      <revision>
        <revnumber>1.2</revnumber>
        <date/>
	<authorinitials>uo</authorinitials>
        <revdescription>
          <para/>
        </revdescription>
      </revision>
    </revhistory>
  </articleinfo>

  <section id="intro">
    <title>Introduction</title>
    <para>
      <ulink url="http://uche.ogbuji.net/tech/4suite/amara">Amara XML Tools</ulink> is a collection of Pythonic tools for XML data binding. Not just tools that
happen to be written in Python, but tools built from the ground up to
use Python idioms and take advantage of the many advantages of Python
over other programming languages.</para>

<para>Amara builds on 4Suite, but whereas 4Suite focuses more on literal
implementation of XML standards in Python, Amara adds a much more
Pythonic face to these capabilities.  The combination ensures standards
compliance within expressive Python form.</para>
    <para>The main component of Amara is:</para>
    <itemizedlist>
      <listitem>
	<para>Bindery: a data binding tool (fancy way of saying it's a very
Pythonic XML API)</para>
      </listitem>
    </itemizedlist>
    <para>Other components are:</para>
    <itemizedlist>
      <listitem>
	<para>Scimitar: an implementation of the ISO Schematron schema language
for XML, which converts Schematron files to Python scripts</para>
      </listitem>
      <listitem>
	<para>domtools: a set of tools to augment Python DOMs</para>
      </listitem>
      <listitem>
      <para>saxtools: a set of tools to make SAX easier to use in Python</para>
      </listitem>
    </itemizedlist>
  </section>
  <section id="getstarted">
    <title>Getting started</title>
    <para>The easiest way to get started is to install Amara and all its dependencies at a stroke using <ulink url="">EasyInstall</ulink>.  Just type <command>easy_install amara</command> and you're all set.  If you run into trouble you may not have EasyInstall.  It's very easy to set up.  If you still run into problems, please report them on the mailing list.
    </para>
    <para>You might choose not to use EasyInstall.  If so, grab the minimally required 4Suite-XML package, install that, then grab Amara and install that using 
using the usual
    <command>python setup.py install</command>, a Windows installer or some other method.</para>
  </section>
  <section id="bindery">
    <title>Amara Bindery: XML as easy as py</title>
    <para>The following example shows how to create a binding from a simple XML
    file, monty.xml. (All example files mentioned are available in the
demo directory of the Amara package.)</para>
    <para>First, the contents of monty.xml:</para>
    <programlisting>
&lt;?xml version="1.0" encoding="utf-8"?&gt;
&lt;monty&gt;
  &lt;python spam="eggs"&gt;
    What do you mean "bleh"
  &lt;/python&gt;
  &lt;python ministry="abuse"&gt;
    But I was looking for argument
  &lt;/python&gt;
&lt;/monty&gt;
    </programlisting>
    <para>Now the code to create the binding:</para>
    <programlisting>
import amara
doc = amara.parse('monty.xml')
    </programlisting>
    <para>
      <command>doc</command> is the data binding result, an object representing the XML. Since I fed the binder a full XML document, I get back an object
representing the document itself which then has a member representing
the top-level element.</para>
    <para>It's that simple. In order to get the value "eggs" (as a Python
Unicode object) you can write:</para>
    <programlisting>
doc.monty.python.spam
    </programlisting>
    <para>Or in order to get the element object with the contents "But I was looking for argument" you can
write:</para>
    <programlisting>
doc.monty.python[1]
    </programlisting>
    <para>The <command>parse</command> function can be passed a file-like object (stream) as well
as a string.  There is also a <command>parse_path</command> function for parsing
XML retrieved from local files and URLs.</para>
    <para>You can pass <command>amara.parse</command> a string (<emphasis>not Unicode object</emphasis>) with the
XML content, an open-file-like object, a file path or a URI.</para>
    <section id="complex-example">
      <title>More complex example</title>
      <para>The following example shows how to create a binding from an XBEL file
(a popular XML format for bookmarks that was developed by Python's
very own XML-SIG). There is a sample XBEL file you can use in the demo
directory.</para>
      <programlisting>
doc = amara.parse('xbel.xml')
      </programlisting>
      <para>The following sample code prints the first and second bookmark titles:</para>
      <programlisting>
print doc.xbel.folder.bookmark.title
print doc.xbel.folder.bookmark[1].title
      </programlisting>
      <para>Note that Bindery tries to make things as natural as possible. You can access child elements by just using their name, usually. If there is
more than one with the same name it grabs the first one. You can use
list indices to specify one of multiple child elements with the same
name. Naturally, a more explicit way of getting the first bookmark's
title is:</para>
      <programlisting>
print doc.xbel.folder.bookmark[0].title
      </programlisting>
      <para>
        <command>title</command> is an element containing only text.  the expression <command>doc.xbel.folder.bookmark[0].title</command> returns the binding object representing the element.  Such objects have unicode conversion methods so that you can get their descendant text (all text nodes in the element's subtree), which is printed in the above line.  The following four lines are all equivalent:</para>
      <programlisting>
print doc.xbel.folder.bookmark.title
print doc.xbel.folder.bookmark[0].title
print unicode(doc.xbel.folder.bookmark.title)
print unicode(doc.xbel.folder.bookmark[0].title)
      </programlisting>
      <para>Calling the <command>unicode</command> conversion on an element node in Amara is very similar to
calling the <command>string</command> conversion on an element node in XPath.</para>
      <para>The following snippet is a recursive function that prints out all bookmark URLs in the file:</para>
      <programlisting>
def all_titles_in_folder(folder):
    #Warning: folder.bookmark will raise an AttributeError if there are no bookmarks
    for bookmark in folder.bookmark:
        print bookmark.href
    if hasattr(folder, "folder"):
        #There are sub-folders
        for folder in folder.folder:
            all_titles_in_folder(folder)
    return

for folder in doc.xbel.folder:
    all_titles_in_folder(folder)
      </programlisting>
      <para>
        <emphasis>You would probably not do this in actual usage, though.</emphasis>  You can perform this task with much less code, without recursion, and with a speed boost using XPath, which is covered <ulink url="#xpath">in a later section</ulink>.</para>
      <para>If you want to count the number of elements of the same name, use <command>len</command>.</para>
      <programlisting>
len(doc.xbel.folder)
      </programlisting>
      <para>This gives the number of top-level folders.</para>
    </section>
    <section id="dtd-validation">
      <title>DTD validation</title>
      <para>You can request that the underlying parser perform DTD validation by setting  <command>validate=True</command> in <command>amara.parse()</command>.</para>
    </section>
    <section id="bindery-workings">
      <title>The workings of Bindery</title>
      <para>In the default binding XML elements turn into specialized objects. For
each generic identifier (element name) a class is generated that is
derived from <command>bindery.element_base</command>. Attributes become simple data
members whose value is a Unicode object containing the attribute
value.</para>
      <para>Element objects are specially constructed so they can be treated as
single objects (in which case the first child element of the
corresponding name is selected, or one can use list item access
notation or even iterate.</para>
      <para>Going back to the example, <command>binding.xbel.folder.bookmark</command> is the same
as <command>binding.xbel.folder.bookmark[0]</command>. Both return the first bookmark
in the first folder. To get the second bookmark in the first folder,
use <command>binding.xbel.folder.bookmark[1]</command>.</para>
    </section>
    <section id="complex-children">
      <title>Complex element children</title>
      <para>Bindery by default preserves ordering information from the source
XML. You can access this through the children list of element and
document objects:</para>
      <programlisting>
folder.xml_children
      </programlisting>
      <para>Within the children list, child elements are represented using the
corresponding binding objects, child text becomes simple Unicode
objects. Notice that in the default binding text children are
normalized, meaning that the binding will never place two text nodes
next to each other in <command>xml_children</command>.</para>
      <para>If an element node contains text as well as child elements, be aware of
the how descendant text nodes are accessed.  You can get the accumulated
text children of an element using the <command>xml_child_text property</command>.  Given
the document <command>&lt;a&gt;1&lt;b&gt;2&lt;/b&gt;3&lt;c/&gt;&lt;/a&gt;</command>, <command>a.xml_child_text</command> would return
<command>u'13'</command>.  On the other hand, converting to Unicode (<command>unicode(a)</command>)
would return <command>u'123'</command>.</para>
    </section>

    <section id="node_structure">
      <title>Checking the structure of nodes</title>
      <para>You can get some information about the structure of most bindery objects
by calling the <command>xml_doc method</command>.</para>
      <programlisting>
&gt;&gt;&gt; import amara
&gt;&gt;&gt; doc = amara.parse('monty.xml')
&gt;&gt;&gt; print doc.xml_doc()
Object references based on XML child elements:
monty (1 element) based on 'monty' in XML
&gt;&gt;&gt; print doc.monty.xml_doc()
Object references based on XML child elements:
python (2 elements) based on 'python' in XML
&gt;&gt;&gt; print doc.monty.python.xml_doc()
Object references based on XML attributes:
spam based on 'spam' in XML
Object references based on XML child elements:
&gt;&gt;&gt; print doc.monty.python.spam
eggs
      </programlisting>
      <para>This is human-readable material, for convenience, but you can also get
node structure information in machine-readable form. <command> xml_properties</command>
returns a dictionary whose keys represent the object reference names from
the XML attributes and elements.</para>
      <programlisting>
&gt;&gt;&gt; import amara
&gt;&gt;&gt; doc = amara.parse("&lt;a x='1'&gt;hello&lt;b/&gt;lovely&lt;c/&gt;world&lt;/a&gt;")
&gt;&gt;&gt; doc.a.xml_properties
{u'x': u'1', u'c': &lt;amara.bindery.c object at 0xb7bbcdcc&gt;, u'b': &lt;amara.bindery.b object at 0xb7bbcb8c&gt;}
      </programlisting>
      <para>
        <command>xml_child_elements</command> returns similar dictionary, but reduced to only the child element.</para>
      <programlisting>
&gt;&gt;&gt; #Continuing from the above snippet
&gt;&gt;&gt; doc.a.xml_child_elements
{u'c': &lt;amara.bindery.c object at 0xb7bbcdcc&gt;, u'b': &lt;amara.bindery.b object at 0xb7bbcb8c&gt;}</programlisting>
    </section>
    <section id="writing-xml">
      <title>Writing XML back out</title>
      <para>The preservation of ordering information means that Bindery does a
pretty good job of allowing you to render binding objects back to XML
form. Use the <command>xml</command> method for this.</para>
      <programlisting>
print doc.xml()
      </programlisting>
      <para>The <command>xml</command> method returns <emphasis>encoded text</emphasis>, not Unicode. The default encoding
is UTF-8. You can also serialize a portion of the document.</para>
      <programlisting>
print doc.xbel.folder.xml() #Just the first folder
      </programlisting>
      <para>You can pass in a stream for the output:</para>
      <programlisting>
doc.xml(sys.stdout)
      </programlisting>
      <para>You can control such matters as the output encoding, whether the
output is pretty-printed, whether there is an output XML declaration,
etc. by using parameters that control the output, based on the XSLT output
control attributes.  As an example, if you pas in <command>omitXmlDeclaration=u"yes"</command>
the output of the XML declaration is suppressed.  Here are the other
parameters you can set.</para>
      <itemizedlist>
<listitem>
          <para>encoding - the character encoding to use (default UTF-8). The writer will automatically use character entities where necessary.</para>
        </listitem>
<listitem>
          <para>omitXmlDeclaration - "yes" to suppress output of the XML declaration. Default "no".</para>
        </listitem>
<listitem>
          <para>standalone - "yes" to set standalone in the XML declaration.</para>
        </listitem>
<listitem>
          <para>mediaType - sets the media type of the output. You'll probably never need this.</para>
        </listitem>
<listitem>
          <para>cdataSectionElements - a list of element names whose output will be wrapped in a CDATA section. This can provide for friendlier output in some cases.</para>
        </listitem>
</itemizedlist>
      <para>You can force Amara to add namespace declarations to an element (or to the root node) even if it's not associated with an element or attribute.  This is especially useful when dealing with QNames in content (A.K.A. hidden namespaces).</para>
      <programlisting>
doc.xml(force_nsdecls={u'x': u'http://example.com/'})
      </programlisting>
      <para><command>force_nsdecls</command> is a dictionary with unicode prefix as the key and unicode namespace URI as the value.  This makes it easy, for example, to force all the known namespace declarations to be at the top (a "sane" document).</para>
      <programlisting>
doc.xml(force_nsdecls=doc.prefixes)
      </programlisting>
      <para>Warning: namespace declarations in the document always trump those forced in this way.  This includes the implicit declaration of the default namespace to null.  In other words you cannot turn a document that doesn't use namespaces into one with a default namespace in one easy stroke as above.  You would have to go through and set the <command>namespaceURI</command> of each element in the document.</para>
    </section>

    <section id="xpath">
      <title>XPath</title>
      <para>Bindery supports an XPath subset that covers almost all of that standard.  The XPath features that are not supported are very rare, and for practical purposes you can assume it's complete XPath support.  The folowing example retrieves all top-level folders:</para>
      <programlisting>
tl_folders = doc.xbel.xml_xpath(u'folder')
for folder in tl_folders:
    print folder.title
      </programlisting>
      <para>You invoke the <command>xml_xpath</command> method on the object you wish to serve as
the context for the XPath query. To get the first element child
(regardless of node name) of the first bookmark of the first folder,
use:</para>
      <programlisting>
doc.xbel.folder.bookmark.xml_xpath(u'*[1]')
      </programlisting>
      <para>or</para>
      <programlisting>
doc.xbel.xml_xpath(u'folder[1]/bookmark[1]/*[1]')
      </programlisting>
      <para>or</para>
      <programlisting>
doc.xbel.xml_xpath(u'/folder[1]/bookmark[1]/*[1]')
      </programlisting>
      <para>or</para>
      <programlisting>
doc.xml_xpath(u'xbel/folder[1]/bookmark[1]/*[1]')
      </programlisting>
      <para>etc.</para>
         <para>
        <emphasis>Warning:</emphasis> in Python, lists indices start with 0 while they start
with 1 in XPath.</para>
        <para>
        <emphasis>Notice</emphasis>: this XPath returns a node set, rendered in Python as a
list of nodes. It happens to be a list of one node, but you still have
to extract it with [0].</para>
      <para>The return value depends on the XPath expression (expr)</para>
      <itemizedlist>
<listitem>
          <para>If expr results in an XPath string, the return value is a Python Unicode object</para>
        </listitem>
<listitem>
          <para>If expr results in an XPath number, the return value is a Python float</para>
        </listitem>
<listitem>
          <para>If expr results in an XPath boolean, the return value is a Python bool object</para>
        </listitem>
<listitem>
          <para>If expr results in an XPath node set, the return value is a Python list (always a list, even if it is empty or contains only one node)</para>
        </listitem>
</itemizedlist>
      <para>The following example prints out all bookmark URLs in the file, but is
much simpler and more compact than the equivalent code <ulink url="#complex-example">earlier in this document</ulink>:</para>
      <programlisting>
bookmarks = doc.xml_xpath(u'//bookmark')
for bookmark in bookmarks:
    print bookmark.href
      </programlisting>
      <para>The following just returns all hrefs
wherever they appear in the document, using an attribute query:</para>
      <programlisting>
hrefs = doc.xml_xpath(u'//@href')
for href in hrefs:
    print unicode(href)
      </programlisting>
      <para>The following prints the title of the bookmark for the 4Suite project:</para>
      <programlisting>
url = u"http://4suite.org/"
title_elements = doc.xml_xpath('//bookmark[@url="%s"]/title'%url)
#XPath node set expression always returns a list
print unicode(title_elements[0])
      </programlisting>
    </section>

    <section id="xslt">
      <title>Applying a transform (XSLT) to a bindery node</title>
      <para>You can apply XSLT directly to a bindery document or element.  You could of course <command>xml()</command> to serialize it and apply XSLT against that, but it's probably easier and a more efficient to work directly on the node.  To do so, use the <command>xml_xslt()</command> method.  <emphasis>Warning:</emphasis> This function is quite limited, and will only handle the
        simplest transforms.  If you find your transform does not work with it,
        serialize using xml() then use Ft.Xml.Xslt.transform, which is fully
        XSLT compliant.
</para>
      <programlisting>
result_string = doc.xml_xslt('transform.xslt')
      </programlisting>
      <para>The one required argument is a reference to a transform.  It can be a a string (not Unicode object), file-like object (stream), file path, URI or
an Ft.Xml.InputSource.InputSource instance.  If string or stream
it must be self-contained  XML (i.e. not requiring access to
any other resource such as external entities or includes).</para>
         <para>The optional <command>param</command> argument is a dictionary of stylesheet parameters, the keys of
            which may be given as unicode objects if they have no namespace,
            or as (uri, localname) tuples if they do.</para>
         <para>The optional <command>output</command> argument is a file-like object to which output is written
            (incrementally, as processed).
</para>
      <para>See the following examples:</para>
      <programlisting>
params = params={u'id' : u'2', (u'http://example.com/ns', u'tags') : [u'a', u'b', u'c']}
result_string = doc.xml_xslt('transform.xslt', params=params)
      </programlisting>
      <para>This would execute the XSLT with overridden values for the <command>id</command> (unprefixed) top level parameter and for the <command>x:tags</command> top level parameter where x is a prefix for the <command>http://example.com/ns</command> namespace.  The latter case provides a node set of text nodes as the parameter.</para>

      <programlisting>
doc.xml_xslt(TRANSFORM_STRING, output=open('/tmp/foo.txt', 'w'))
      </programlisting>
      <para>Would execute the XSLT provided in the string, with output streaming into teh file <command>/tmp/foo.txt</command> (remember that XSLT output can be text, XML or HTML).  There is no return value since <command>output</command> is specified.</para>

      <programlisting>
result_string = doc.xml_xslt(open('transform.xslt'))
      </programlisting>
      <para>Read the transform from an open file object.</para>

     </section>

    <section id="namespaces">
      <title>Namespaces</title>
      <para>Bindery supports documents with namespaces. The following example
displays a summary of the contents of an RSS 1.0 feed:</para>
      <programlisting>
import amara

#Set up customary namespace bindings for RSS
#These are used in XPath query and XPattern rules
RSS10_NSS = {
    u'rdf': u'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
    u'dc': u'http://purl.org/dc/elements/1.1/',
    u'rss': u'http://purl.org/rss/1.0/',
    }

doc = amara.parse('rss10.rdf', prefixes=RSS10_NSS)

#Create a dictionary of RSS items
items = {}
item_list = doc.xml_xpath(u'//rss:item')
items = dict( [ ( item.about, item) for item in item_list ] )
print items

for channel in doc.RDF.channel:
    print "Channel:", channel.about
    print "Title:", channel.title
    print "Items:"
    for item_ref in channel.items.Seq.li:
        item = items[item_ref.resource]
        print "\t", item.link
        print "\t", item.title
      </programlisting>
      <para>The following illustrates how namespace details are maintained in
bindery objects:</para>
      <programlisting>
#Show the namespace particulars of the rdf:RDF element
print doc.RDF.namespaceURI
print doc.RDF.localName
print doc.RDF.prefix
      </programlisting>
      <para>For attributes, <command>xml_attributes</command> is a dictionary containing namespace
information for all of an element's attributes. See the Attributes
section below for more details.</para>
      <para>Namespaces work naturally with XPath as well:</para>
      <programlisting>
#Get the RSS item with a given URL
item_url = u'http://www.oreillynet.com/cs/weblog/view/wlg/532'
matching_items = doc.RDF.xml_xpath(u'//rss:item[@rdf:about="%s"]'%item_url)
print matching_items
assert matching_items[0].about == item_url
      </programlisting>
      <para>In the above example I manually set the mapping from namespace prefixes to namespace names, but if your use of XML namespaces is "sane", you might not need this step.  Bindery document objects automatically remember the namespace declarations made on the top level element of any document you parse.</para>
    </section>
    <section id="naming">
      <title>Naming things</title>
      <para>The Python object reference and class names used in Amara bindings are based on the corresponding XML IDs, but there are limits to such mappings.
For one thing, XML allows characters that are not allowed in Python IDs,
such as <command>-</command>.  In such cases Amara mangles the name, using underscores by default.  In the case of a document such as <command><![CDATA[<a-1 b-1=""/>]]></command> you would access the element using <command>doc.a_1</command>, and the attribute using <command>doc.a_1.b_1</command>.</para>
      <para>This can be problematic when writing generic code to address XML, because any element's name might be mangled in a different way depending on document context.  You always have the option of accessing objects using their proper XML names in XPath:</para>
      <para>
        <command>doc.xml_xpath(u"a-1/b-1")</command>
      </para>
      <para>You can also use Python mapping protocol to access objects:</para>
      <para>
        <command>doc[u'a-1'][u'b-1']</command>
      </para>
      <para>This is equivalent to:</para>
      <para>
        <command>doc[None, u'a-1'][None, u'b-1']</command>
      </para>
      <para>The <command>None</command> is the namespace name, which of course you should specify as a Unicode object if the desired object is in fact in a namespace in the original document.  Amara allows one further level of disambiguation:</para>
      <para>
        <command>from xml.dom import Node
E = Node.ELEMENT_NODE
doc[E, None, u'a-1'][E, None, u'b-1']
</command>
      </para>
      <para>This allows you to handle the very rare situation where an attribute name clashes with that of a child element of its owner.  For example, in <command><![CDATA[<a-1 b-1=""><b-1/></a-1>]]></command> you can access the element <command>b-1</command> as above, and the attribute of the same name using <command>doc[E, None, u'a-1'][A, None, u'b-1']</command>, assuming you have <command>A = Node.ATTRIBUTE_NODE</command>.</para>
      <para>You can get the original XML name information from any object using
properties named after DOMs:</para>
      <itemizedlist>
	<listitem>
	  <para>
            <command>element.nodeName</command>
          </para>
	</listitem>
	<listitem>
	  <para>
            <command>element.localName</command>
          </para>
	</listitem>
	<listitem>
	  <para>
            <command>element.namespaceURI</command>
          </para>
	</listitem>
	<listitem>
	  <para>
            <command>element.prefix</command>
          </para>
	</listitem>
      </itemizedlist>
      <para>And you can get similar information on attributes by reading the <command>xml_attributes</command> dictionary on the element node.</para>
    </section>
    <section id="pushbind">
      <title>Push binding</title>
      <para>If you're dealing with a large XML file, you may not want the entire data binding in memory at the same time. You may want to instantiate it bit by bit. If you have a clear pattern for how you want to break up the document, you can use the function <command>amara.pushbind</command>. See the following example:</para>
      <programlisting>
import amara

for folder in amara.pushbind('xbel.xml', u'/xbel/folder'):
    title = folder.title
    bm_count = len(list(folder.bookmark))
    print "Folder", title, "has", bm_count, "top level bookmarks"
      </programlisting>
      <para>The neat thing is that this program doesn't have the entire binding in memory at time. In each iteration it loads just enough XML to represent each top-level folder element. <command>pushbind</command> is a generator that yields each little subtree each time it's invoked.</para>
      <para>In general <command>pushbind</command> subtrees are Amara bindery objects based on the XSLT pattern that is passed in as its first argument. You also pass in an XML source, either a string (use the <command>string= keyword</command>) or a URI or file-name (use the <command>source= keyword</command>).</para>      <para>An interactive session helps illustrate:</para>
      <programlisting>
&gt;&gt;&gt; XML="""\
... &lt;doc&gt;
...   &lt;one&gt;&lt;a&gt;0&lt;/a&gt;&lt;a&gt;1&lt;/a&gt;&lt;/one&gt;
...   &lt;two&gt;&lt;a&gt;10&lt;/a&gt;&lt;a&gt;11&lt;/a&gt;&lt;/two&gt;
... &lt;/doc&gt;
... """
&gt;&gt;&gt; import amara
&gt;&gt;&gt; chunks = amara.pushbind(XML, u'a')
&gt;&gt;&gt; a = chunks.next()
&gt;&gt;&gt; print a
0
&gt;&gt;&gt; print a.xml()
&lt;a&gt;0&lt;/a&gt;
&gt;&gt;&gt; a = chunks.next()
&gt;&gt;&gt; print a.xml()
&lt;a&gt;1&lt;/a&gt;
&gt;&gt;&gt; a = chunks.next()
&gt;&gt;&gt; print a.xml()
&lt;a&gt;10&lt;/a&gt;
&gt;&gt;&gt; a = chunks.next()
&gt;&gt;&gt; print a.xml()
&lt;a&gt;11&lt;/a&gt;
&gt;&gt;&gt; a = chunks.next()
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in ?
StopIteration
      </programlisting>
      <para>In the above case the XSLT pattern "a" matched all the elements with this name in the file.  All the XML outside the "a" elements is essentially discarded by this code, so you have to tailor the XSLT pattern to include all the material you're interested in.  In the following example, only the first two "a" elements are included in the generator yield.</para>
      <programlisting>
&gt;&gt;&gt; chunks = amara.pushbind(XML, u'one/a')
&gt;&gt;&gt; a = chunks.next()
&gt;&gt;&gt; print a.xml()
&lt;a&gt;0&lt;/a&gt;
&gt;&gt;&gt; a = chunks.next()
&gt;&gt;&gt; print a.xml()
&lt;a&gt;1&lt;/a&gt;
&gt;&gt;&gt; a = chunks.next()
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in ?
StopIteration
      </programlisting>
      <para>The pattern <command>/doc/one/a</command> would result in similar behavior for the sample document.</para>
      <para>You can use namespaces in these patterns by using prefixes defined in a dictionary passed to <command>pushbind</command>.</para>
      <programlisting>
import amara
#Set up customary namespace bindings for RSS
#These are used in XPath query and XPattern rules
RSS10_NSS = {
u'rdf': u'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
u'dc': u'http://purl.org/dc/elements/1.1/',
u'rss': u'http://purl.org/rss/1.0/',
}

#Print out all titles in the RSS feed
items = amara.pushbind('demo/rss10.rdf', u'rss:item',
                               prefixes=RSS10_NSS)
for item in items:
    print item.title
#Print out all titles in the RSS feed, slightly different approach
chunks = amara.pushbind('demo/rss10.rdf', u'rss:item/rss:title',
                               prefixes=RSS10_NSS)
for title in chunks:
    print title

      </programlisting>
    </section>
    <section id="modification">
      <title>Modification</title>
      <para>Modifying a binding is pretty straightforward. You can create or
modify an attribute by simple assignment:</para>
      <programlisting>
import amara
doc = amara.parse('monty.xml')
doc.monty.foo = u'bar'
doc.monty.spam = u'[attr modified]'
      </programlisting>
      <para>You can also replace an element's contents with a single text node,
using similar notation:</para>
      <programlisting>
doc.monty.python = u'[elem 1 modified]\n'
doc.monty.python[1] = u'[elem 2 modified]\n'
      </programlisting>
      <para>The resut of the above code is:</para>
      <programlisting>
&lt;monty&gt;
  &lt;python spam="[attr modified]" foo="bar"&gt;[elem 1 modified]
&lt;/python&gt;
  &lt;python ministry="abuse"&gt;[elem 2 modified]
&lt;/python&gt;
&lt;/monty&gt;
      </programlisting>
      <para>You can empty out all children of an element:</para>
      <programlisting>
doc.monty.python.xml_clear()
      </programlisting>
      <para>And add new elements and text.  Create a new, empty element named <command>new</command>
and append it as the last childof the first <command>python</command> element.</para>
      <programlisting>
doc.monty.python.xml_append(doc.xml_create_element(u'new'))
      </programlisting>
      <para>Append a text node.</para>
      <programlisting>
doc.monty.python.new.append(u'New Content')
      </programlisting>
      <para>You can insert new elements or text into specific locations, either before or after an existing child.</para>
      <programlisting>
#Create a new `python` element as the second element child of `monty`
doc.monty.xml_insert_after(doc.monty.python,
                           doc.xml_create_element(u'python'))
#Create a new `python` element as the first element child of `monty`
doc.monty.xml_insert_before(doc.monty.python,
                            doc.xml_create_element(u'python'))
      </programlisting>
      <para>You can also delete a specific element, attribute, or text child:</para>
      <programlisting>
del doc.monty.python
      </programlisting>
      <para>which does the same thing as</para>
      <programlisting>
del doc.monty.python[0]
    </programlisting>
      <para>You can also use the <command>xml_remove_child</command> method:</para>
      <programlisting>
child = doc.monty.python
doc.monty.xml_remove_child(child)
      </programlisting>
      <para>Just to exhaustively list the approaches to deletion, you can use the position of an object among its siblings to remove it from its parent.
You can get this position using the <command>xml_index_on_parent</command> property.</para>
      <programlisting>
ix = doc.monty.python.xml_index_on_parent
      </programlisting>
      <para>This assigns ix the value 1 since the first python element is the
second child of monty.</para>
       <programlisting>
ix = doc.monty.python[1].xml_index_on_parent
      </programlisting>
      <para>This assigns <command>ix</command> the value 3 since the second python element is the fourth child of <command>monty</command>. Once you have an index, you can use that index in order to delete a specific child by passing it to the <command>xml_remove_child_at</command> method:</para>
      <programlisting>
doc.monty.xml_remove_child_at(3)
      </programlisting>
      <para>This removes the second python element, using the index determined
above. This works for text as well:</para>
      <programlisting>
doc.monty.xml_remove_child_at(0)
      </programlisting>
      <para>Removes the first text node.  You can omit the index in the call to
this method. By default it removes the last child:</para>
      <programlisting>
doc.monty.xml_remove_child_at()
      </programlisting>
      <para>If you run into the sort of identifier naming issues mentioned in the "Naming Things" section you can use the mapping protocol to make modifications.  For example to remove the "b-1" child element from</para>
      <programlisting>
<![CDATA[<a-1 b-1=""><b-1/></a-1>]]>
      </programlisting>
      <para>One option is:</para>
      <programlisting>
from xml.dom import Node
E = Node.ELEMENT_NODE
del doc[E, None, u'a-1'][E, None, u'b-1']
      </programlisting>
    </section>
    <section id="createelem">
      <title>Creating elements (and attributes)</title>
      <para>You can create a new element with a namespace:</para>
      <programlisting>
e = doc.xml_create_element(element_qname, element_ns)
      </programlisting>
      <para>which is equivalent to</para>
      <programlisting>
e = doc.xml_create_element(element_qname, namespace=element_ns)
      </programlisting>
      <para>You can easily add attributes while you're creating elements.</para>      <programlisting>
import amara
doc = amara.parse('monty.xml')
#Create a third python element
e = doc.xml_create_element(u'python', attributes={u'life': u'brian'})
doc.monty.xml_append(e)
print doc.xml()
      </programlisting>
      <para>This gives the following output:</para>
      <programlisting>
&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;monty&gt;
  &lt;python spam="eggs"&gt;
    What do you mean "bleh"
  &lt;/python&gt;
  &lt;python ministry="abuse"&gt;
    But I was looking for argument
  &lt;/python&gt;
&lt;python life="brian"/&gt;&lt;/monty&gt;
      </programlisting>
      <para>You can see how the attribute is manifested on the new element.</para>
      <para>The dictionary <command>attributes={u'life': u'brian'}</command> is actually a short-hand. The full form is:</para>
      <programlisting>
{
  (&lt;attr1_qname&gt;, &lt;attr1_namespace&gt;): attr1_value},
  (&lt;attr2_qname&gt;, &lt;attr2_namespace&gt;): attr2_value},
  ...
  (&lt;attrN_qname&gt;, &lt;attrN_namespace&gt;): attrN_value},
}
      </programlisting>
      <para>But you can abbreviate <command>(&lt;attrN_qname&gt;, &lt;attrN_namespace&gt;)</command> to just <command>&lt;attrN_qname&gt;</command> if the namespace is None (i.e. the attribute is
not in a namespace).</para>
      <para>So you could add a namespace qualified attribute as follows:</para>
      <programlisting>
import amara
NS = u'urn:bogus'
doc = amara.parse('monty.xml')
#Create a third python element
e = doc.xml_create_element(
     u'python',
     attributes={(u'ns:life', NS): u'brian'},
     content=u'unfortunate'
     )
doc.monty.xml_append(e)
print doc.xml()
     </programlisting>
      <para>Notice that this time I threw in some content as well. The result:</para>
      <programlisting>
&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;monty&gt;
  &lt;python spam="eggs"&gt;
    What do you mean "bleh"
  &lt;/python&gt;
  &lt;python ministry="abuse"&gt;
    But I was looking for argument
  &lt;/python&gt;
&lt;python xmlns:ns="urn:bogus" ns:life="brian"&gt;unfortunate&lt;/python&gt;&lt;/monty&gt;
      </programlisting>
    </section>
    <section id="attrmod">
      <title>Modifying attributes</title>
      <para>To create an attribute after the element is created, use the
<command>xml_set_attribute</command> method. To add the namespace
qualified attribute from the example above, use the following:</para>
      <programlisting>
import amara
NS = u'urn:bogus'
doc = amara.parse('monty.xml')
#Create a third python element
e = doc.xml_create_element(
          u'python',
          content=u'unfortunate'
          )
doc.monty.xml_append(e)
doc.monty.python[2].xml_set_attribute((u'ns:life', NS), u'brian')
print doc.xml()
      </programlisting>
      <para>This produces the same XML as above. If no namespace is required, the first argument to <command>xml_set_attribute</command> is just the attribute name.</para>
      <para>The <command>xml_set_attribute</command> method returns the name of the resulting attribute.</para>
      <para>You can set an attribute's value using Python idiom as well:</para>
      <programlisting>
doc.monty.python[2].life = u'Pi'
      </programlisting>
      <para>Information about an element's attributes, including namespace
information, is kept in <command>xml_attributes</command>. This is a dictionary keyed by the local name of each attribute, with the value being a tuple of
the namespace qualified attribute name and the namespace URL. For
example, given the following code:</para>
      <programlisting>
import amara
NS = u'urn:bogus'
doc = amara.parse('monty.xml')
#Create a third python element
e = doc.xml_create_element(
  u'python',
  content=u'unfortunate'
)
doc.monty.xml_append(e)
#Add a namespace qualified attribute
doc.monty.python[2].xml_set_attribute((u'ns:life', NS), u'brian')
#Add an attribute with no namespace
doc.monty.python[2].xml_set_attribute(u'foo', u'bar')
      </programlisting>
      <para>
        <command>doc.monty.python[2].xml_attributes</command> gives the value:</para>
      <programlisting>
{u'life': (u'ns:life', u'urn:bogus'), u'foo': (u'foo', None)}
      </programlisting>
      <para>Just for fun, here's an interesting variation that illustrates the
special status of the XML namespace.</para>
      <programlisting>
import amara
from xml.dom import XML_NAMESPACE as XML_NS
doc = amara.parse('monty.xml')
#Create a third python element
e = doc.xml_create_element(
          u'python',
          attributes={(u'xml:lang', XML_NS): u'en'},
          content=u'Ni!'
          )
doc.monty.xml_append(e)
print doc.xml()
     </programlisting>
      <para>This gives the following output:</para>
      <programlisting>
&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;monty&gt;
  &lt;python spam="eggs"&gt;
    What do you mean "bleh"
  &lt;/python&gt;
  &lt;python ministry="abuse"&gt;
    But I was looking for argument
  &lt;/python&gt;
&lt;python xml:lang="en"&gt;Ni!&lt;/python&gt;&lt;/monty&gt;

      </programlisting>
      <para>Notice that there's no declaration for the XML namespace, as allowed by the standard.</para>
    </section>
    <section id="xmlfrag">
      <title>Appending XML fragments</title>
      <para>Amara offers a powerful facility for adding to XML documents through the <command>xml_append_fragment</command> method on elements.  You pass this method a string (<emphasis>not Unicode</emphasis>, since this is a parse operation) with a fragment of literal XML which is parsed and added to the element.  The XML fragment must be a well formed external parsed entity.  Basically multiple root elements are allowed, but they must be properly balanced, special characters escaped, and so on.  Doctype declaration is prohibited.  According to XML rules, the encoded string is assumed to be UTF-8 or UTF-16, but you can override this with an XML text declaration (<command>&lt;?xml version="1.0" encoding="ENC"?&gt;</command>) or by passing in an encoding parameter to this function.</para>
      <programlisting>
import amara
doc = amara.parse('monty.xml')
doc.monty.xml_append_fragment('&lt;py3 x="1"&gt;p&lt;/py3&gt;&lt;py4 y="2"&gt;q&lt;/py4&gt;')
print doc.monty.xml_child_elements.keys()
      </programlisting>
      <para>The output is <command>[u'python', u'py3', u'py4']</command>, as two elements are added in the <command>xml_append_fragment</command> call.</para>
      <para>The optional encoding is a string with the encoding to be used in parsing the XML fragment.  If this parameter is specified, it overrrides any text
declaration in the XML fragment.</para>
      <programlisting>
#Latin-1 ordinal 230 is the a-e ligature
doc.monty.xml_append_fragment('&lt;q&gt;P%an&lt;/q&gt;'%chr(230), 'latin-1')
      </programlisting>
    </section>
    <section id="createdoc">
      <title>Creating full documents</title>
      <para>You can create entire documents from scratch</para>
      <programlisting>
doc = amara.create_document()
doc.xml_append(doc.xml_create_element(u"hello"))
doc.xml()
      </programlisting>
      <para>Yields</para>
      <programlisting>
&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;hello/&gt;
      </programlisting>
      <para>You can specify a root element to be created in the empty document.  The following code:</para>
      <programlisting>
doc = amara.create_document(u"hello")
doc.hello.xml_append(doc.xml_create_element(u"world"))
doc.xml()
      </programlisting>
      <para>Yields</para>
      <programlisting>
&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;hello&gt;&lt;world/&gt;&lt;/hello&gt;
      </programlisting>
      <para>This is equivalent to:</para>
      <programlisting>
doc = amara.create_document()
doc.xml_append(doc.xml_create_element(u"hello"))
doc.hello.xml_append(doc.xml_create_element(u"world"))
doc.xml()
      </programlisting>
      <para>You can set a namespace on the root element using the <command>ns</command> parameter.  There are many other useful parameters.  Try <command>import amara; help(amara.create_document)</command> at a Python prompt for more details.</para>
    </section>
    <section id="deepcopies">
      <title>Making deep copies of nodes</title>
      <para>If you're familiar with XSLT, you might wonder how to do the equivalent of xsl:copy-of in Amara.  You can create such a deep copy using the <command>copy</command> module in the Python standard library.</para>
      <programlisting>
import copy
import amara
doc = amara.parse('monty.xml')
#Clone the document
doc2 = copy.deepcopy(doc)
#This modification only affects the clone
doc2.monty.python.spam = u"abcd"

#This output will just like what was read in
print doc.xml()
#This output will show the change from "eggs" to "abcd"
print doc2.xml()
      </programlisting>
    </section>
    <section id="picomments">
      <title>Processing instructions and comments</title>
      <para>Bindery supports these XML constructs in a fairly natural way. If you have PIs or comments in a source document parsed into a binding, it
will have objects representing the PIs and comments:</para>
      <programlisting>
import amara
DOC = """\
&lt;?xml-stylesheet url="xxx.css" type="text/css"?&gt;
&lt;!--A greeting for all--&gt;
&lt;hello-world/&gt;
"""
doc = amara.parse(DOC)
print doc.xml_children
      </programlisting>
      <para>shows the following list:</para>
      <programlisting>
[
&lt;amara.bindery.pi_base instance at 0x433f6c&gt;,
&lt;amara.bindery.comment_base instance at 0x433fac&gt;,
&lt;amara.bindery.hello_world object at 0x433fec&gt;
]
      </programlisting>
      <para>The first item is a bound PI object and the second a bound
comment. You can dig deeper if you like:</para>
      <programlisting>
pi = doc.xml_children[0]
comment = doc.xml_children[1]
print repr(pi.target) #shows u'xml-stylesheet'
print repr(pi.data) #shows u'url="xxx.css" type="text/css"'
print repr(comment.data) #shows u'A greeting for all'
      </programlisting>
      <para>You can also create or mutate these objects.</para>
      <programlisting>
doc = amara.create_document()
pi = bindery.pi_base(u"xml-stylesheet", u'url="xxx.css" type="text/css"')
doc.xml_append(pi)
doc.xml_append(doc.xml_create_element(u"A"))
      </programlisting>
    </section>
    <section id="doctypes">
      <title>Document types</title>
      <para>There is also an API for document type declarations (DTDecls).</para>
      <para>To create a document with a DTDecl, do something like the following:</para>
      <programlisting>
doc = amara.create_document(
    u"xsa",
    pubid=u"-//LM Garshol//DTD XML Software Autoupdate 1.0//EN//XML",
    sysid=u"http://www.garshol.priv.no/download/xsa/xsa.dtd"
    )
      </programlisting>
      <para>Which results in a tree equivalent to:</para>
      <programlisting>
&lt;?xml version="1.0" encoding="utf-8"?&gt;
&lt;!DOCTYPE xsa PUBLIC "-//LM Garshol//DTD XML Software Autoupdate 1.0//EN//XML"
                     "http://www.garshol.priv.no/download/xsa/xsa.dtd"&gt;
&lt;xsa/&gt;
      </programlisting>
      <para>Notice how this automatically creates the document element for you (no need for a separate <command>xml_append</command>). You can expand on this to create attributes and content for the document element:</para>
      <programlisting>
from xml.dom import XML_NAMESPACE as XML_NS

doc = amara.create_document(
    u"xsa",
    attributes={(u'xml:lang', XML_NS): u'en'},
    content=u' ',
    pubid=u"-//LM Garshol//DTD XML Software Autoupdate 1.0//EN//XML",
    sysid=u"http://www.garshol.priv.no/download/xsa/xsa.dtd"
    )
      </programlisting>
      <para>Which results in:</para>
      <programlisting>
&lt;?xml version="1.0" encoding="utf-8"?&gt;
&lt;!DOCTYPE xsa PUBLIC "-//LM Garshol//DTD XML Software Autoupdate 1.0//EN//XML"                     "http://www.garshol.priv.no/download/xsa/xsa.dtd"&gt;
&lt;xsa xml:lang="en"&gt; &lt;/xsa&gt;
      </programlisting>
      <para>You can then access the DTDecl details:</para>
      <programlisting>
assert doc.xml_pubid == u"-//LM Garshol//DTD XML Software Autoupdate 1.0//EN//XML" 
assert doc.xml_sysid == u"http://www.garshol.priv.no/download/xsa/xsa.dtd"
assert doc.xml_doctype_name == u"xsa"
      </programlisting>
      <section id="future">
        <title>Future doctype support from parse</title>
        <para>The idea is that if you parse a document with a DTDecl, the root node contains the document element QName, the public ID and the system ID. This does not work yet because of idiosyncracies of the Python/XML libraries. This should be fixed when I remove dependencies on these libraries in a coming version. When it does work, you should be able to do:</para>
        <programlisting>
#DOES NOT YET WORK

XSA = """\
&lt;?xml version="1.0" encoding="utf-8"?&gt;
&lt;!DOCTYPE xsa PUBLIC "-//LM Garshol//DTD XML Software Autoupdate 1.0//EN//XML"                     "http://www.garshol.priv.no/download/xsa/xsa.dtd"&gt;
&lt;xsa&gt;
  &lt;vendor&gt;
    &lt;name&gt;Fourthought, Inc.&lt;/name&gt;
    &lt;email&gt;info@fourthought.com&lt;/email&gt;
    &lt;url&gt;http://fourthought.com&lt;/url&gt;
  &lt;/vendor&gt;
  &lt;product id="FourSuite"&gt;
    &lt;name&gt;4Suite&lt;/name&gt;
    &lt;version&gt;1.0a1&lt;/version&gt;
    &lt;last-release&gt;20030327&lt;/last-release&gt;
    &lt;info-url&gt;http://4suite.org&lt;/info-url&gt;
    &lt;changes&gt;
 - Begin the 1.0 release cycle
    &lt;/changes&gt;
  &lt;/product&gt;
&lt;/xsa&gt;
"""
doc = amara.parse(XSA)
assert doc.xml_pubid == u"-//LM Garshol//DTD XML Software Autoupdate 1.0//EN//XML"
assert doc.xml_sysid == u"http://www.garshol.priv.no/download/xsa/xsa.dtd"
assert doc.xml_doctype_name == u"xsa"
        </programlisting>
        <para>Internal DTD subset constructs are not preserved in the binding.</para>
      </section>
    </section>
    <section id="custom-binding">
      <title>Customizing the binding</title>
      <para>Bindery works by iterating over XML nodes and firing off a set of
rules triggered by the node type and other details. The default
binding is the result of the default rules that are registered for
each node type, but Bindery makes this easy to tweak by letting you
register your own rules.</para>
      <para>Bindery comes bundled with 3 easy rule frameworks to handle some
common binding needs.</para>
      <section id="simple-string">
        <title>Treating some elements as simple string values</title>
        <para>The title elements in XBEL are always simple text, and creating full Python objects for them is overkill in most cases. They could be just
as easily simple data members with the Unicode value of the element's
content. To make this adjustment in Bindery, register an instance of
the <command>simple_string_element_rule</command> rule. This rule takes an list of XSLT pattern expressions which indicate which elements are to be
simplified. So to simplify all title elements:</para>
        <programlisting>
import amara
from amara import binderytools
#Specify (using XSLT patterns) elements to be treated similarly to attributes
rules = [
    binderytools.simple_string_element_rule(u'title')
    ]
#Execute the binding
doc = amara.parse('xbel.xml', rules=rules)

#title is now simple unicode
print doc.xbel.folder.bookmark.title.__class__
	</programlisting>
      </section>
      <section id="omit-elem">
        <title>Omitting certain elements entirely</title>
	<para>Perhaps you want to focus on only part of a document, and to save
memory and hassle, you want to omit certain elements that are not of
interest in the binding. You can use the <command>omit_element_rule</command> in this case.</para>
        <para>The following example does not create bindings for folder titles at all (but bookmark titles are preserved):</para>
        <programlisting>
import amara
from amara import binderytools
#Specify (using XSLT patterns) elements to be ignored
rules = [
    binderytools.omit_element_rule(u'folder/title')
    ]
#Execute the binding
doc = amara.parse('xbel.xml', rules=rules)

#Following would now raise an exception:
#print doc.xbel.folder.title
        </programlisting>
      </section>
          <section id="omit-nodetype">
                <title>Omitting certain node types entirely</title>
                <para>You can also omit processing instructions, comments or text nodes from a document using the <command>omit_nodetype_rule</command> rule.  The rule takes a single parameter which can be one of the three node types <command>xml.dom.Node.COMMENT_NODE</command>, <command>xml.dom.Node.PROCESSING_INSTRUCTION_NODE</command> or <command>xml.dom.Node.TEXT_NODE</command>.</para>
                <para>In the following example there are no bindings created for comments:</para>
                <programlisting><![CDATA[import amara
from amara import binderytools
from xml.dom import Node

DOCUMENT = """<!-- Printing the best language --> <language>Python</language>"""

rules = [binderytools.omit_nodetype_rule(Node.COMMENT_NODE)]

doc = amara.parse(DOCUMENT, rules = rules)

print doc.xml()]]>
                </programlisting>
                <para>With the resulting output:</para>
                <programlisting><![CDATA[<?xml version="1.0" encoding="UTF-8"?>
<language>Python</language> 
                      ]]>
                </programlisting>
          </section>
          <section id="wsstripping">
        <title>Stripping whitespace</title>
        <para>A common need is to strip out pure whitespace nodes so that they don't clutter up "children" lists. Bindery bundles the <command>ws_strip_element_rule</command> rule for this purpose.  Elements that match the pattern are stripped of whitespace.</para>
        <programlisting>
import amara
from amara import binderytools
#Specify (using XSLT patterns) elements to be stripped
#In this case select all top-level elements for stripping
rules = [
    binderytools.ws_strip_element_rule(u'/*')
    ]
#Execute the binding
doc = amara.parse('xbel.xml', rules=rules)
        </programlisting>
        <para>You can combine rules, such as stripping white space while still
omitting certain elements.</para>
      </section>
      <section id="element-skeleton">
        <title>Creating an element skeleton</title>
        <para>If all you care about is the structure of elements and attributes, and not the text content you can use the <command>element_skeleton_rule</command>.</para>
        <para>Elements that match the pattern have all character data stripped.</para>
        <programlisting>
import amara
from amara import binderytools
#Specify (using XSLT patterns) elements to be bound as skeletons
#In this case select all elements
rules = [
    binderytools.element_skeleton_rule(u'*')
    ]
#Execute the binding
doc = amara.parse('xbel.xml', rules=rules)
        </programlisting>
      </section>
      <section id="typeinf">
        <title>The type inferencer</title>
        <para>The basic idea behind data binding is translating XML into native data types. Amara provides a rule that looks at each XML node to see if it can infer a native Python data type for the value, in particular int, float or datetime.</para>
        <programlisting>
TYPE_MIX = """\
&lt;?xml version="1.0" encoding="utf-8"?&gt;
&lt;a a1="1"&gt;
  &lt;b b1="2.1"/&gt;
  &lt;c c1="2005-01-31"&gt;
    &lt;d&gt;5&lt;/d&gt;
  &lt;e&gt;2003-01-30T17:48:07.848769Z&lt;/e&gt;
  &lt;/c&gt;
  &lt;g&gt;good&lt;/g&gt;
&lt;/a&gt;"""

import amara
from amara import binderytools
rules=[binderytools.type_inference()]
doc = amara.parse(TYPE_MIX, rules=rules)
doc.a.a1 == 1     #type int
doc.a.b.b1 == 2.1 #type float
doc.a.c.c1 == datetime.datetime(2005, 1, 31) #type datetime.
        </programlisting>
      </section>
      <section id="rules-namespaces">
        <title>Using namespaces in custom rules</title>
        <para>The built-in custom rules use XSLT patterns, which use prefixes to specify namespaces. You may have to let the binder tools know what namespace bindings are in effect:</para>
        <programlisting>
import amara
from amara import binderytools
#Set up customary namespace bindings for RSS
#These are used in XPath query and XPattern rules
RSS10_NSS = {
    'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
    'dc': 'http://purl.org/dc/elements/1.1/',
    'rss': 'http://purl.org/rss/1.0/',
    }

rules = [
    binderytools.simple_string_element_rule(u'title')
    ]
#Execute the binding
doc = amara.parse('rss10.rdf', prefixes=RSS10_NSS, rules=rules)
        </programlisting>
        <para>Remember, however, as dicussed above, if you declare all the namespaces you use on top-level elements, you do not need to repeat them in the explicit <command>prefixes</command> dictionary.</para>
      </section>
    </section>
    <section id="rules-pushbind">
      <title>Push binding and rules</title>
      <para>You can also use rules with pushbind.  If all you ever want from "a" elements is to extract the text content, you could do something like the following.  Look carefully: the sample document is slightly different this time.</para>
      <programlisting>
&gt;&gt;&gt; XML="""\
... &lt;doc&gt;
...   &lt;one&gt;&lt;a&gt;0&lt;/a&gt;&lt;b&gt;1&lt;/b&gt;&lt;/one&gt;
...   &lt;two&gt;&lt;a&gt;10&lt;/a&gt;&lt;b&gt;11&lt;/b&gt;&lt;/two&gt;
... &lt;/doc&gt;
... """
&gt;&gt;&gt; import amara
&gt;&gt;&gt; from amara import binderytools
&gt;&gt;&gt; #This rule says "treat all elements at the third level of depth as simple strings"
&gt;&gt;&gt; rule = binderytools.simple_string_element_rule(u'/*/*/*')
&gt;&gt;&gt; #Push back bindings of all second level elements ('one' and 'two')
&gt;&gt;&gt; chunks = amara.pushbind(XML, u'/*/*', rules=[rule])
&gt;&gt;&gt; elem = chunks.next()
&gt;&gt;&gt; print elem.a.__class__
&lt;type 'unicode'&gt;
&gt;&gt;&gt; print elem.a
u'0'
&gt;&gt;&gt; print elem.b.__class__
&lt;type 'unicode'&gt;
&gt;&gt;&gt; print elem.b
u'1'
      </programlisting>
    </section>
    <section id="custom-binding-classes">
      <title>Using custom binding classes</title>
      <para>If you need more sophisticated tweaking, you proably want to register your own customized binding class. The following example gives bookmark elements a method, <command>retrieve</command>, which retrieves the body of the Web page:</para>

<!--
      <programlisting>
import urllib
from xml.dom import Node
import amara
from amara import bindery
from Ft.Xml import InputSource
from Ft.Lib import Uri

#Subclass from the default binding class
#We're adding a specialized method for accessing a bookmark on the net
class specialized_bookmark(bindery.element_base):
    def retrieve(self):
        try:
            stream = urllib.urlopen(self.href)
            content = stream.read()
            stream.close()
            return content
        except IOError:
            import sys; sys.stderr.write("Unable to access %s\n"%self.href)

#Explicitly create a binder instance, in order to customize rules
binder = bindery.binder()

#associate specialized_bookmark class with elements not in an XML
#namespace and having a GI of "bookmark"
binder.set_binding_class(None, "bookmark", specialized_bookmark)

#Execute the binding
doc = amara.parse('xbel.xml', binderobj=binder)

#Show specialized instance
print doc.xbel.folder.bookmark.__class__

#Exercise the custom method
print "Content of first bookmark:"
print doc.xbel.folder.bookmark.retrieve()
      </programlisting>
-->

      <programlisting>
import urllib
from xml.dom import Node
import amara
from amara import bindery

#Subclass from the default binding class
#We're adding a specialized method for accessing a bookmark on the net
class specialized_bookmark(bindery.element_base):
    def retrieve(self):
        try:
            stream = urllib.urlopen(self.href)
            content = stream.read()
            stream.close()
            return content
        except IOError:
            import sys; sys.stderr.write("Unable to access %s\n"%self.href)

doc = amara.parse(XML, binding_classes={(None, u'bookmark'): specialized_bookmark})

#Show specialized instance
print doc.xbel.folder.bookmark.__class__

#Exercise the custom method
print "Content of first bookmark:"
print doc.xbel.folder.bookmark.retrieve()
      </programlisting>
      <para>Focus on the line:</para>
      <programlisting>
doc = amara.parse(XML, binding_classes={(None, u'bookmark'): specialized_bookmark})
      </programlisting>
      <para>When you register classes to use in binding a given elements type you do so by specifying namespace URI and local name of the element. If you know that the element is not in a namespace, as in the XBEL example, you use <command>None</command>. <command>None</command> is the Right Way to signal "not in a namespace" in most Python/XML tools, and not the empty string <command>""</command>.</para>
        <para>See also the <command>accesstrigger.py</command> demo.</para> 
      <section id="custom-binding-warning">
        <title>General warning about customized bindings</title>
        <para>Bindery tries to manage things so that writing back the XML from a binding makes sense, and that XPath gives expected results, but it is easy to bring about odd results if you customize the binding.</para>
        <para>As an exampe, if you use <command>simple_string_element_rule</command> and then reserialize using the <command>xml</command> method, the elements that were simplified will be written back out as XML attributes rather than child elements. If you do run into such artifacts after customizing a binding the usual remedy is to write a custoized <command>xml</command> method or add  specialized XPath wrapper code (see <command>bonderyxpath.xpath_wrapper_mixin</command> for the default XPath wrappering).</para>
      </section>
    </section>
    <section id="extensions">
      <title>Bindery extension guide</title>
      <para>Bindery is designed to be extensible, but this is not a simple
proposition given the huge flexibility of XML expression, and the many
different ways developpers might want to generate resulting Python
objects (and vice versa). You can pretty much do whatever you need to
by writing Bindery extensions, but in order to keep things basically
manageable, there are some ground rules.</para>
      <section id="laws">
        <title>Bindery laws:</title>
	<orderedlist>
	  <listitem>
	    <para>Binding objects corresponding to an XML document have a single root object from which all other objects can be reached through navigating attributes (no, fancy method calls don't count)</para>
	  </listitem>
	</orderedlist>
	<para>[TODO: more on this section to come. If you try tweaking bindery extensions and have some useful notes, please pitch in by sending them along.]</para>
      </section>
    </section>
  </section>
  <section id="scimitar">
  <title>Scimitar: the most flexible schema language for the most flexible programming language</title>
  <para>Scimitar is an implementation of ISO Schematron that compiles a
  Schematron schema into a Python validator script.</para>
  <para>Scimitar supports all of the draft ISO Schematron specification. See
  the TODO file for known gaps in Scimitar convenience.</para>
  <para>You typically use scimitar in two phases. Say you have a schematron
  schema schema1.stron and you want to validate multiple XML files
against it, instance1.xml, instance2.xml, instance3.xml.</para>
    <para>First you run schema1.stron through the scimitar compiler script,
scimitar.py:</para>
    <programlisting>
scimitar.py schema1.stron
    </programlisting>
    <para>A file, schema1.py (same file stem with the "py" extension
sunstituted), is generated in the current working directory. If you'd
prefer a different location or file name, use the "-o" option. The
generated file is a validator script in Python. It checks the
schematron rules specified in schema1.stron.</para>
    <para>You now run the generated validator script on each XML file you wish
to validate:</para>
    <programlisting>
python schema1.py instance1.xml
   </programlisting>
    <para>The validation report is generated on standard output by default, or
you can use the "-o" option to redirect it to a file.</para>
    <para>The validation report is an XML external parsed entity, in other words
a file that is much like a well-formed XML document, but with some
restrictions loosened so that it's effectively text with possible
embedded tags.</para>
    <para>To elaborate using the example from the schematron 1.5 specification:</para>
    <programlisting>
$ cat simple1.stron
&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;sch:schema xmlns:sch="http://www.ascc.net/xml/schematron" version="ISO"&gt;
 &lt;sch:title&gt;Example Schematron Schema&lt;/sch:title&gt;
 &lt;sch:pattern&gt;
   &lt;sch:rule context="dog"&gt;
    &lt;sch:assert test="count(ear) = 2"
    &gt;A 'dog' element should contain two 'ear' elements.&lt;/sch:assert&gt;
    &lt;sch:report test="bone"
    &gt;This dog has a bone.&lt;/sch:report&gt;
   &lt;/sch:rule&gt;
  &lt;/sch:pattern&gt;
&lt;/sch:schema&gt;

$ scimitar.py simple1.stron
$ ls simple*.py
simple1-stron.py
$ cat instance2.xml
&lt;dog&gt;&lt;ear/&gt;&lt;/dog&gt;

$ python simple1-stron.py instance2.xml
&lt;?xml version="1.0" encoding="UTF-8"?&gt;
Processing schema: Example Schematron Schema

Processing pattern: [unnamed]

Assertion failure:
A 'dog' element should contain two 'ear' elements.

    </programlisting>
  </section>
  <section id="domtools">
    <title>Amara DOM Tools: giving DOM a more Pythonic face</title>
    <para>DOM came from the Java world, and hardly the most Pythonic API
possible (see the Bindery above for a good step forward). Some
DOM-like implementations such as 4Suite's Domlettes mix in some
Pythonic idiom. Amara DOM Tools goes even further in this regard.</para>
    <section id="pushdom">
      <title>The pushdom</title>
      <para>You're probably familiar with <command>xml.dom.pulldom</command>, which offers a nice hybrid between SAX and DOM, allowing you to efficiently isolate important parts of a document in a SAX-like manner, and then using DOM for finer-grained manipulation. Amara's pushdom makes this process even more convenient You give it a set of XPatterns, and it provides a generator yielding a series of DOM chunks according to the patterns.</para>
      <para>In this way you can process huge files with very little memory usage, but most of the convenience of DOM.</para>
      <programlisting>
for docfrag in domtools.pushdom('demo/labels.xml', u'/labels/label'):
    label = docfrag.firstChild
    name = label.xpath('string(name)')
    city = label.xpath('string(address/city)')
    if name.lower().find('eliot') != -1:
        print city.encode('utf-8')
      </programlisting>
      <para>Prints "Stamford".</para>
      <para>See also <ulink url="http://lists.xml.org/archives/xml-dev/200412/msg00606.html">this XML-DEV message</ulink>.</para>
    </section>
    <section id="domtools-generators">
      <title>Generator tools</title>
      <para>For more on the generator tools see the article "<ulink url="http://www.xml.com/pub/a/2003/01/08/py-xml.html">Generating DOM
Magic</ulink>".</para>
    </section>
    <section id="domtools-xpath">
      <title>Getting an XPath for a given node</title>
      <para>
        <command>domtools.abs_path</command> allows you to get the absolute path for a node. The following code:</para>
      <programlisting>
from amara import domtools
from Ft.Xml.Domlette import NonvalidatingReader
from Ft.Lib import Uri
file_uri = Uri.OsPathToUri('labels.xml', attemptAbsolute=1)
doc = NonvalidatingReader.parseUri(file_uri)

print domtools.abs_path(doc)
print domtools.abs_path(doc.documentElement)
for node in doc.documentElement.childNodes:
    print domtools.abs_path(node)
      </programlisting>
      <para>Displays:</para>
      <programlisting>
/
/labels[1]
/labels[1]/text()[1]
/labels[1]/label[1]
/labels[1]/text()[2]
/labels[1]/label[2]
/labels[1]/text()[3]
/labels[1]/label[3]
/labels[1]/text()[4]
/labels[1]/label[4]
/labels[1]/text()[5]
      </programlisting>
      <para>For more on abs_path tools see the article "<ulink url="http://www.xml.com/pub/a/2004/11/24/py-xml.html">Location, Location, Location</ulink>".</para>
    </section>
  </section>
  <section id="saxtools">
    <title>Amara SAX Tools: SAX without the brain explosion</title>
    <para>Tenorsax (<command>amara.saxtools.tenorsax</command>) is a framework for "linerarizing" SAX logic so that it flows a bit more naturally, and needs a lot less state machine wizardry.</para>
    <para>I haven't yet had time to document it heavily, but see
test/saxtools/xhtmlsummary.py for an example.</para>
    <para>See also this <ulink url="http://lists.xml.org/archives/xml-dev/200412/msg00605.html">XML-DEV message</ulink>.</para>
  </section>
  <section id="flextyper">
    <title>Flextyper: user-defined datatypes in Python for XML processing</title>
    <para>Flextyper is an implementation of Jeni Tennison's Data Type Library Language (DTLL) (on track to become part 5 of ISO Document Schema Definition Languages (DSDL). You can use Flextyper to generate Python modules containing data types classes that can be used with 4Suite's RELAX NG library</para>
    <para>Flextyper is currently experimental. It won't come into its full usefulness until the next release of 4Suite, although you can use it with current CVS releases of 4Suite.</para>
    <para>Flextyper compiles a DTLL file into a collection of Python modules implementing the contained data types. Run it as follows:</para>
    <programlisting>
flextyper.py dtll.xml
   </programlisting>
    <para>A set of files, one per data type namespace defined in the DTLL, is
created. By default the output file names are based on the input,
e.g. dtll-datatypes1.py, dtll-datatypes2.py, etc.</para>
    <para>You can now register these data types modules with a processor instance of 4Suite's RELAX NG implementation.</para>
  </section>
</article>
```