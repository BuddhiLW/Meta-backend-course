# Table of Contents

1.  [Schedule](#orgb4d2b9f)
2.  [Introduction to Back-end Development](#org571438d)
    1.  [Week 1](#orgd780178)
        1.  [Capstone project overview](#orgeb0b08c)
        2.  [How the web works](#org0fd7855)
        3.  [Grace Egbo - a day in the life of a backend dev.](#orgd5b1b72)
        4.  [How the internet works](#orgd82cefd)
        5.  [Servers](#org66588ad)
        6.  [What are websites and webpages?](#org060ee53)
        7.  [TCP - Transmission Control Protocol](#orgaf0b74c)
        8.  [UDP - User Datagram Protocol](#orgbb60324)
        9.  [HTTP - HyperText Transfer Protocol](#orgb46ae85)
        10. [Makeup of a HTTP request](#org296f63a)
        11. [Makeup of a HTTP response](#org8948915)
        12. [Examples about HTTP](#orgd436045)
        13. [IDEs](#org5371e53)
        14. [Extra resources](#org3a0a114)
    2.  [Week 2](#org12fbac4)
        1.  [HTML](#orgbdcdbe2)
        2.  [DOM](#orgb5403d2)
        3.  [CSS](#orga5377ef)
        4.  [Extra Resources](#orgb0f7260)
    3.  [Week 3](#orge32d840)
        1.  [Working with libraries](#org5cb2689)
        2.  [Responsive Design](#orgcfecfc3)
        3.  [Types of Grids](#org81830b8)
        4.  [Bootstrap](#org2deef47)
        5.  [Static vs Dinamic websites](#org10beb66)
        6.  [SPA and Multi-Page Application](#orgae27ef9)
        7.  [**React**](#org0e63d09)
        8.  [Extra resources](#orgb9b4226)
3.  [Programming in Phyton](#org0bc9e81)
    1.  [Objectives](#org104696a)
    2.  [Week1-Notes - Introduction to Python](#org2a89d92)
        1.  [Course content](#orgb264ef4)
        2.  [Input](#orgc3a9256)
        3.  [Format](#orgc3ecd66)
        4.  [Match](#orgb89cb22)
    3.  [Week2-Notes - Python Data structures](#orgaa205a9)
        1.  [\*args, \*\*kwargs](#org7a4ef4a)
        2.  [Additional Resources](#org8ae71eb)
        3.  [Open, close files](#org473b519)
        4.  [Read files](#orgf4bcb29)
        5.  [Extra Resources](#org3366ad0)
    4.  [Week3-Notes - Programming Paradigms](#org2871dea)
        1.  [What is procedural programming?](#org4820afb)
        2.  [Functional programming](#org00e3d20)
        3.  [Slice functions](#org412c053)
        4.  [Recursive reversal](#org1b8933b)
        5.  [`map` and `filter`](#org855daf1)
        6.  [Assignment - list comprehension](#orge2fe286)
        7.  [Object Oriented Programing (OOP)](#org238d64a)
        8.  [Extra resources](#orgde094ec)
    5.  [Week4-notes - Modules, Packages, Libraries and Testing](#org507c361)
        1.  [Imports](#orgbc4b7ec)
        2.  [Scopes](#orga4c038b)
        3.  [Additional Resource](#org77ac697)
        4.  [Most common libraries](#orgc8364eb)
        5.  [Examples of libraries-use](#orgeddca00)
        6.  [More on Big Data and Analysis in Python](#org2282ad8)
        7.  [Web Frameworks](#orgc81e020)
        8.  [Additional Resources](#orgf2720d8)
        9.  [Features of using libraries for testing](#org2ba6af2)
        10. [What `testing` must have](#org2313c48)
        11. [Testing Life Cycle](#org6334af5)
        12. [Good testing leads to](#org64488c1)
        13. [Types of testing](#org97d4e25)
        14. [How to know there was sufficient testing](#orgb7930c8)
        15. [Deep-in types of testing](#org0b82843)
        16. [Levels of testing](#orgea0499b)
        17. [Testing in Python](#orgd5b24c1)
        18. [Pytest testing](#orgec18445)
        19. [TDD (Test-Driven Development)](#org1f68493)
        20. [Other types of development cycles](#orgf7fb4ac)
        21. [Examples TDD](#org610139f)
        22. [Additional Resources](#org130ad09)
        23. [Final Test](#orge9d965d)
4.  [Version Control](#org9cc9700)

Back-end development by [Meta, on Coursera](https://www.coursera.org/professional-certificates/meta-back-end-developer).

<a id="orgb4d2b9f"></a>

# Schedule

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">

<colgroup>
<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">Monday</th>
<th scope="col" class="org-left">Tuesday</th>
<th scope="col" class="org-left">Wednesday</th>
<th scope="col" class="org-left">Thursday</th>
<th scope="col" class="org-left">Friday</th>
<th scope="col" class="org-left">Saturday</th>
<th scope="col" class="org-left">Sunday</th>
</tr>
</thead>

<tbody>
<tr>
<td class="org-left">8h-8h45m</td>
<td class="org-left">x</td>
<td class="org-left">x</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">x</td>
<td class="org-left">&#xa0;</td>
</tr>

<tr>
<td class="org-left">9h-9h45m</td>
<td class="org-left">x</td>
<td class="org-left">x</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">x</td>
<td class="org-left">&#xa0;</td>
</tr>

<tr>
<td class="org-left">10h-10h45m</td>
<td class="org-left">x</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">x</td>
<td class="org-left">&#xa0;</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="org-left">13h-13h45m</td>
<td class="org-left">x</td>
<td class="org-left">x</td>
<td class="org-left">x</td>
<td class="org-left">x</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">x</td>
</tr>

<tr>
<td class="org-left">14h-14h45m</td>
<td class="org-left">x</td>
<td class="org-left">x</td>
<td class="org-left">x</td>
<td class="org-left">x</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">x</td>
</tr>

<tr>
<td class="org-left">15h-15h45m</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">x</td>
<td class="org-left">x</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">x</td>
</tr>
</tbody>

<tbody>
<tr>
<td class="org-left">17h30m-18h15m</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">x</td>
<td class="org-left">x</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>

<tr>
<td class="org-left">18h30m-19h15m</td>
<td class="org-left">x</td>
<td class="org-left">x</td>
<td class="org-left">x</td>
<td class="org-left">x</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>

<tr>
<td class="org-left">19h30m-20h15m</td>
<td class="org-left">x</td>
<td class="org-left">x</td>
<td class="org-left">x</td>
<td class="org-left">x</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>
</tbody>
</table>

<a id="org571438d"></a>

# Introduction to Back-end Development

<a id="orgd780178"></a>

## Week 1

<a id="orgeb0b08c"></a>

### Capstone project overview

1.  TODO Create Django web server, with multilple API endpoints.

2.  TODO Connect it to a MySQL database.

3.  TODO Create a template system driven by Django views.

<a id="org0fd7855"></a>

### How the web works

1.  Fullstack

    Both front and back development. Mostly, on connecting the two.

    - Planning.
    - Architecture.
    - Design.
    - Development.
    - Deployment.
    - Maintenance.

2.  Front-end

    Design patterns of elements on a page.

3.  Back-end

    - Back-end language.
    - Database.
    - APIs.
    - Web servers

<a id="orgd5b1b72"></a>

### Grace Egbo - a day in the life of a backend dev.

The day breaks out in sections.

1.  Code review

2.  Possible quick fixes

3.  Meeting about ideias and needs

4.  Coding

5.  Soft skills/People skills

    - Communicate.
    - Listen to perspectives.
    - Remote world makes that even more necessary.

<a id="orgd82cefd"></a>

### How the internet works

1.  Definition: `Network`

    Two or more computers connected through wired or wireless connection.

    1.  Multiples devices in a network - Network Switches

        - Complexity is brough down by using `Network switches`.

2.  Definition: `Interconnected network`

    When multiple `Networks` connect through `Netowork Switches`.
    E.g., the `Internet`.

    [![img](./img/internet-scheme.png "Client-server connection through the Intertnet")](img/internet-scheme.png)

<a id="org66588ad"></a>

### Servers

- Data centers: multitude of servers on a physical space.
- `Server purpose` _data center_ will have different machinery, depending on the application objetive.

1.  Webservers

    - Website hosting.
    - Database.
    - Control panel.
    - CMS software.
    - Email.

    [![img](./img/web-server.png "“What is a web server and how does it work?”, by Meta")](img/web-server.png)

    1.  Web request

        `Request-response cycle`:

        > It&rsquo;s the job of the web server to send you back those website content, upon requesting, by typing the URL of the website.

        Designed to respond to thousands of requests of clients per second.

<a id="org060ee53"></a>

### What are websites and webpages?

1.  Webpage

    Display content, like text, images, videos etc, on the web browser.

2.  Website

    It&rsquo;s a collection of web pages linked together.

3.  HTML, CSS and JavaScript

    1.  HTML

        `Hyperlink Text Markup Language`
        Tells how to structure elements in a page.

    2.  CSS

        Cascade Styling Sheets.

    3.  JavaScript

        Programming language build into the browser.
        Tools for `interactivity`, `data-processing` and `control-and-action`.

    4.  Page rendering process

        > While interpreting each line of HTML, the browser creates a building-block that
        > switches the visual representation you see on screen.

        A response from the webserver must be a complete web page, in other to fulfill
        the request, to show the page, in the browser.

    5.  Web browsers

        Software application used to browse the world-wide-web.

        It works by sending a request to a web server, and then receives a response
        containing the content to be displayed on your device.

        1.  URL

            `Uniform Resource Locator`, contains the protocol (HTTP/HTTPS), the domain name,
            and the file-path.

        2.  HTTP

            - HyperText Transfer Protocol.
            - Request-response cycle.

<a id="orgaf0b74c"></a>

### TCP - Transmission Control Protocol

- Transmits messages with high precision.
- Barley no data loss.
- Almost always on the right addresses.
- Slower than UDP.

<a id="orgbb60324"></a>

### UDP - User Datagram Protocol

- Corrupt package issue solved (barely no data loss).
- Easily out of order data-packages.
- Possibly a lot of loss of information.

<a id="orgb46ae85"></a>

### HTTP - HyperText Transfer Protocol

- Standard for the web communication.
- Transfers data:
  - Web pages,
  - Images,
  - Files.
- Request-response based communication between client and server.

<a id="org296f63a"></a>

### Makeup of a HTTP request

It must contain a

- Method,
- Path,
- Version,
- Headers.

1.  Method

    > Describes the kind of action that the client wants to perform.

    Most common are:

    - GET;
    - POST;
    - PUT;
    - DELETE;

    1.  Get

        Retrieves information.

    2.  Post

        Sends information.

    3.  Put

        Update data on webserver. That is, data1 is swapped for data2.

    4.  Delete

        Removes the resource.

2.  Path

    > The path is a representation of where the resource is located on the webserver.

3.  Version

    > Rules of what constitutes and how request and response happen.

4.  Headers

    > Headers contains additional information about the request and the client that is making the request.

<a id="org8948915"></a>

### Makeup of a HTTP response

It&rsquo;s similar to HTTP requests.

After the `header`, the `message body` contains data that is the response:

- Text.
- HTML Markup.
- Images.
- Files.
- etc.

1.  Header

    - HTTP response status (200, 404, 400, etc.).
    - Status message (OK, Not Found, Server Not Responding, etc.).

    1.  Informational

        Responses ranging 100-199.

        - Provisional.
        - Interim response.
        - Most common: 100 CONTINUE.

    2.  Successful

        Responses ranging 200-299.

        If successfully processed (200 OK),

        - GET: Found/included.
        - POST: Successfully transmitted.
        - PUT: Successfully transmitted.
        - DELETE: Deleted.

    3.  Redirection

        Responses ranging 300-399.

        - 301 MOVED PERMANENTLY.
        - 302 FOUND.

    4.  Client error

        Responses ranging 400-499.

        - 400 BAD DATA (transmitted to the server);
        - 401 MUST LOGIN (before making the request);
        - 403 REFUSE TO PROCESS (but valid request);
        - 404 NOT FOUND (requested data);

    5.  Server error

        Responses ranging 500-599.

        - 500 INTERNAL SERVER ERROR (server failed to process request);

<a id="orgd436045"></a>

### Examples about HTTP

1.  **Request Line**

    > Every HTTP request begins with the request line.
    >
    > This consists of the HTTP method, the requested resource and the HTTP protocol
    > version.
    >
    > `GET /home.html HTTP/1.1`
    >
    > In this example, `GET` is the HTTP method, `/home.html` is the resource
    > requested and HTTP 1.1 is the protocol used.

2.  HTTP Method

<a id="org5371e53"></a>

### IDEs

`Integrated Development Environment` offers:

- Syntax highlight;
- Keyword documentation;
- Auto-complete suggestions;
- Navigation ease;
- Unified Environment for development;

<a id="org3a0a114"></a>

### Extra resources

HTTP Overview (Mozilla)

<https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview>

Introduction to Networking by Dr.Charles R Severance

<https://www.amazon.com/Introduction-Networking-How-Internet-Works/dp/1511654945/>

Chrome Developer Tools Overview (Google)

<https://developer.chrome.com/docs/devtools/overview/>

Firefox Developer Tools User Docs (Mozilla)

<https://firefox-source-docs.mozilla.org/devtools-user/index.html>

Getting Started with Visual Studio Code (Microsoft)

<https://code.visualstudio.com/docs>

<a id="org12fbac4"></a>

## Week 2

<a id="orgbdcdbe2"></a>

### HTML

1.  Table

2.  Forms

3.  Input tags

    - Text;
    - Password;
    - Checkbox;
    - Radio;
    - Textarea;
    - Select;

<a id="orgb5403d2"></a>

### DOM

`Document Object Model`
Server -> Web browser receives webpage -> Transforms in a DOM scheme.

<a id="orga5377ef"></a>

### CSS

How to display HTML elements.

- Selector (which element to act upon);
- Key-values:
  - Property;
  - Property-value;

<a id="orgb0f7260"></a>

### Extra Resources

1.  HTML and DOM

    Learn more​
    Here is a list of resources that may be helpful as you continue your learning journey.

    HTML Elements Reference (Mozilla)

    <https://developer.mozilla.org/en-US/docs/Web/HTML/Element>

    The Form Element (Mozilla)

    <https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form>

    What is the Document Object Model? (W3C)

    <https://www.w3.org/TR/WD-DOM/introduction.html>

    ARIA in HTML (W3C via Github)

    <https://w3c.github.io/html-aria/>

    ARIA Authoring Practices (W3C)

    <https://www.w3.org/TR/wai-aria-practices-1.2/>

<a id="orge32d840"></a>

## Week 3

<a id="org5cb2689"></a>

### Working with libraries

Libraries can depend on other libraries forming a tree of dependencies.

- Bundlers unify all code in one file, or few of them.
- Finally, add the final bundled file into your HTML.

<a id="orgcfecfc3"></a>

### Responsive Design

A `responsive grid` happens when we combine:

- Flexible grids;
- Fluid images;
- Media queries.

1.  Flexible grids

    - Gutter: space between contents;
    - Margin: space between content and screen;
    - Sizes based on percentages.

2.  Fluid images

    - Max-width: 100%;
      - Shrink based on container-element size;
    - Fit on page;
    - Never grow larger than original size.

3.  Media queries

    Controls:

    - Display size;
    - Orientation;
    - Aspect ratio.

<a id="org81830b8"></a>

### Types of Grids

- Fixed grid;
- Fluid grid;
- Hybrid grid;

1.  Fixed Grid

    - Fixed width-columns;
    - Flexible-margins;

2.  Fluid grid

    - Fluid width-columns;
    - Fixed-gutters;
    - Fixed-margins;

    Columns either grow or shrink to adapt to the available space.

3.  Hybrid grid

    - Fluid and fixed width components;
    - Different rules, depending on device;
    - Optimize experience.

<a id="org2deef47"></a>

### Bootstrap

1.  Responsive design with class infix

    Convention for `class infix` made for `responsive design`, by **Bootstrap**.

    [![img](./img/bootstrap.png)](img/bootstrap.png)

2.  Class modifiers

    It&rsquo;s like the conjugation of verbs, so you have different meaning, with the same functionality. E.i., buttons of alert that can mean &ldquo;just pay attention&rdquo;, or &ldquo;**DANGER!**&rdquo; etc.

<a id="org10beb66"></a>

### Static vs Dinamic websites

1.  Static part of a website

    - Images;
    - Videos;
    - Text.

2.  Dinamic part of a website

    Static content that is generated, depending on the response of an `application server`.

    To speed up the process and don&rsquo;t overload the website, `cache` is used to store dynamically generated content.

    [![img](./img/cache.png)](img/cache.png)

<a id="orgae27ef9"></a>

### SPA and Multi-Page Application

1.  Multi-page Application

    - Loads all content at each update
    - Application server return the entire webpage

2.  SPA

    SPA can use both `bundling` and `lazy-load` to display dynamic content.

    1.  Bundling

        When a new component or data is requested the hole section is returned and rendered.

    2.  Lazy-loading

        When a new piece of a component or data is requested, only the fraction of data and component concerned for the request is loaded.

<a id="org0e63d09"></a>

### **React**

<a id="orgb9b4226"></a>

### Extra resources

1.  Bootstrap

    Bootstrap Official Website

    <https://getbootstrap.com/>

    Bootstrap 5 Foundations by Daniel Foreman

    <https://www.amazon.com/Bootstrap-Foundations-Mr-Daniel-Foreman/dp/B0948GRS8W/>

    Responsive Web Design with HTML5 and CSS by Ben Frain

    <https://www.amazon.com/Responsive-Web-Design-HTML5-CSS/dp/1839211563/>

    Bootstrap Themes

    <https://themes.getbootstrap.com/>

2.  React

    Learn more​
    Here is a list of resources that may be helpful as you continue your learning journey.

    React Official Website
    <https://reactjs.org/>

    Choosing between Traditional Web Apps and Single Page Apps (Microsoft)

    <https://docs.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/choose-between-traditional-web-and-single-page-apps>

    React Source Code (Github)

    <https://github.com/facebook/react>

    Introduction to React.js

    The original video recorded at Facebook in 2013.

    <https://youtu.be/XxVg_s8xAms>

<a id="org0bc9e81"></a>

# Programming in Phyton

<a id="org104696a"></a>

## Objectives

Get started with the Python programming language and associated foundational concepts.

**Learning Objectives:**

- Recognize common applications of the Python programming language.
- Explain foundational software engineering concepts.
- Use operators to program a simple output in Python.
- Use control flow and loops to solve a problem

<a id="org2a89d92"></a>

## Week1-Notes - Introduction to Python

<a id="orgb264ef4"></a>

### Course content

> Course content  
> During this course, you’ll cover everything you need to begin with Python development. The content of the four modules is listed below.
>
> **Module 1 - Getting started with Python**
> In this module, you will get an introduction to the course and you’ll cover a brief summary of the history of programming. You will also learn the basics of how programming works and discover typical uses for Python in real-life. There are also some tips on how to take this course successfully.
>
> Before embarking on any coding you’ll first establish if your current computer system is set up correctly and identify any required operating system dependencies. Then you’ll explore different ways that you can run programs through Python.
>
> Next, you’ll study Python syntax using comments, variables, data types and user input and output. You’ll proceed to expand your Python skills by using math and logical operators so you can control the flow of your code and perform operations such as addition, subtraction, division, and multiplication.
>
> Python has multiple ways to do code loops or looping. You will examine looping constructs to iterate your code over multiple sequences.
>
> **Module 2 - Basic programming with Python**
> In module 2, you&rsquo;ll receive an introduction to Python functions, including how to declare a function, and how to pass data to a function or return data from a function. You will also explore data structures, scope, and the concepts of lists and how they can be used in Python. You will also discover tuples, sets, dictionaries and kwargs, gaining an understanding of how their main uses.
>
> Errors and exceptions are two very important aspects of learning Python as a new developer. In module 2, you will start with errors and exceptions, and explore what happens when something goes wrong with your code. Exception handling and Python file handling are covered, as are how to create files in Python and various methods of inserting content into a new file.
>
> **Module 3 - Programming paradigms**
> In the third module, you will cover programming paradigms, and look at the features and concepts behind procedural programming, functional programming and object oriented programming.
>
> A key feature of procedural programming is algorithms, you will explore how they can be used to solve problems, how algorithmic complexity is calculated and learn about Big-O notation.
>
> Next you will learn about pure functions and recursion in functional programming, as well as the difference between maps and filters.
>
> Finally, you will explore object-oriented programming and its four main concepts. ​ You will explore the relationship between classes and instances in Python by creating classes, instantiating them, and accessing their variables and methods. You’ll learn about abstract classes and methods and how to implement them. The rules of method resolution and inheritance with child and parent classes are also explained. Being able to read files is essential when working with stored data in Python and you’ll discover several built-in functions to make this easier.
>
> **Module 4 - Modules, packages, libraries and tools**
> In module 4, you learned that Python is a powerful language that allows you to build amazing things. But it can gain even more functionality with the use of modules, libraries and tools. You will learn about Modules and that they are the building blocks for adding functionality to your code, so you don’t need to continually redo everything.
>
> You will also explore some of the commonly used Python libraries in data analysis and data science, and how they can apply to the areas of machine learning and artificial intelligence.
>
> Finally, you’ll find out why testing is an essential component of Quality Assurance and explore the type of testing you should use. You will learn about test automation packages and the importance of automated testing and you’ll write some tests using PyTest. Finally, you will explore the evolution of Test-driven development (or TDD), and focus on how to apply a test-driven development methodology.
>
> **Module 5 - Graded assessment**
> Here you&rsquo;ll learn about the graded assessment. After you complete the individual items in this module, you&rsquo;ll test your knowledge and skills by completing an end of course graded assessment.

<a id="orgc3a9256"></a>

### Input

    ipt = input("Please input something")
    print(inp)

<a id="orgc3ecd66"></a>

### Format

    a=1
    b="abb"
    print("{0} is different from {1}" .format(a, b))

<a id="orgb89cb22"></a>

### Match

    http = 200
    match http:
        case 200:
            print("ok!")
        _:
            print("anything else!")

    a = isinstance(str, "aa")

    print(a)

<a id="orgaa205a9"></a>

## Week2-Notes - Python Data structures

<a id="org7a4ef4a"></a>

### \*args, \*\*kwargs

1.  Args

        def s(*args):
            return sum(args)

        print(s(3,4,5,6))

        def s(*args):
            return sum(*args)

        print(s([3,4,5,6]))

2.  Kwargs

        def s(**kwargs):
            return sum()

        print(s(3,4,5,6))

<a id="org8ae71eb"></a>

### Additional Resources

1.  First

    Python allows you to do quite a lot with very little code. Compared to other languages such as Java or C#, Python has a much easier learning curve. It lends itself well to the &ldquo;write less, do more philosophy&rdquo;. Python developers are also in high demand and learning how to program in Python makes for a good career choice.

    You can access the links below to learn more about programming in Python.

    Check out the Python website to find out more about built-in functions:
    Python

    Check out W3 Schools to learn more about coding and web development:
    W3Schools

    Check out HackerRank to practice your new acquired Python skills:
    HackerRank

2.  Data Structures

    Here is a list of resources that may be helpful as you continue your learning journey.

    Learn more about Python data structures (Python documentation) on the Python website:
    Python.org - Data structures

    Explore common Python data structures at the Real Python website:
    Real Python - Data structures

<a id="org473b519"></a>

### Open, close files

1.  Open files

    1.  options

        - `r`: read (text)
        - `rb`: read (binary)
        - `r+`: read and write
        - `w`: write (overwrite file)
        - `a`: append data

    2.  `with open`

        No need to use the `close` function.

            with open('testing.txt', 'r') as file:

2.  Close files

    - No arguments.

3.  Examples

    1.  Open and read

            file = open('test.txt', mode='r')

            data = file.readline()

            print(data)

            file.close()

            # alternative
            with open('test.txt', mode='r') as file:
                data = file.readline()
                print(data)

            Hello there!

    2.  Create file and populate it

            try:
                with open('sample/newfile.txt', 'w') as file:
                    file.writelines(["Hello", "\nThere", "\nThird line!"])

                with open('sample/newfile.txt', 'a') as file:
                    file.writelines(["\nHello", "\nThere", "\nThird line!"])
            except FileNotFoundError as e:
                print("Error: ", e)

<a id="orgf4bcb29"></a>

### Read files

1.  Complete file

        with open('samplefile.txt', 'r') as file:
            print(file.read())

2.  Only selected characters

        with open('samplefile.txt', 'r') as file:
            print(file.read(40))

3.  Read a line

    Reads the entire line:

        with open('samplefile.txt', 'r') as file:
            print(file.readline())

    Reads the line until the _nth_ character:

        n=10
        with open('samplefile.txt', 'r') as file:
            print(file.readline(n))

4.  Read multiple lines

    `readlines()` read the entire contents of the file and returns it in an ordered list,

        with open('samplefile.txt', 'r') as file:
            lines=file.readlines()
            print(len(lines))

            for line in lines:
                print(line)

5.  Looping through lines

    `with open() as file` already returns a list of lines stored in `file`.

        with open('samplefile.txt', 'r') as file:
            for line in file:
                print(line)

<a id="org3366ad0"></a>

### Extra Resources

The following resources will be helpful as additional references in dealing with different concepts related to the topics you have covered in this module.

Learn more about exceptions and errors in Python on the Python website:
Exceptions and Errors in Python - Python docs

Check out the PyNative website to learn more about file handling in Python:
File handling in Python

<a id="org2871dea"></a>

## Week3-Notes - Programming Paradigms

Principle `DRY`:

- Don&rsquo;t;
- Repeat;
- Yourself.

<a id="org4820afb"></a>

### What is procedural programming?

Creating reusable code that is used multiple times, so to DRY.

<a id="org00e3d20"></a>

### Functional programming

    # Recursive function for Tower of Hanoi
    def hanoi(disks, source, helper, destination):
        print('P1 - disk: {}, source: {}, helper: {}, destination: {}'.format(disks, source, helper, destination))
        # Base Condition
        if (disks == 1):
            print('Disk {} moves from tower {} to tower {}.'.format(disks, source, destination))
            return

        # Recursive calls in which function calls itself
        hanoi(disks - 1, source, destination, helper)
        print('P2 - disk: {}, source: {}, helper: {}, destination: {}'.format(disks, source, helper, destination))
        print('Disk {} moves from tower {} to tower {}.'.format(disks, source, destination))
        hanoi(disks - 1, helper, source, destination)
        print('P3 - disk: {}, source: {}, helper: {}, destination: {}'.format(disks, source, helper, destination))

    # Driver code
    # disks = int(input('Number of disks to be displaced: '))
    disks = 3
    '''
    Tower names passed as arguments:
    Source: A
    Helper: B
    Destination: C
    '''
    # Actual function call
    hanoi(disks, 'A', 'B', 'C')

<a id="org412c053"></a>

### Slice functions

    # str[start:stop:step]
    trial = "rbvcrsal"
    new_trial = trial[::-1]
    print(new_trial)
    print("---", range(len(trial)), "---")
    print(trial[len(trial):-(len(trial)+1):-1])
    print(new_trial == trial[len(trial):-(len(trial)+1):-1])
    for i in range(len(trial)):
        print(trial[i::-1])
        # print(trial[i:-(len(trial)+1):-1])

<a id="org1b8933b"></a>

### Recursive reversal

    trial="abcdefg"

    # Idea: concatenate string in the opposite order
    print(trial)
    print("trial[1:]: ", trial[1:], ", trial[0]: ", trial[0], sep='')
    print("trial[2:]: ", trial[2:], ", trial[1]: ", trial[1], ", trial[0]: ", trial[0], sep='')
    # trial[0] -> get first character in string
    def first_character(str):
        return str[0]

    def string_opposite(str):
        if len(str) == 0:
            return "" # empty string -> always will concatenate the empty string in last call
        else:
            # get first character and concatenate (at the end),
            # with the reversed string of the orginial string, less the first character.
            return string_opposite(str[1:]) + first_character(str)

    print(string_opposite(trial))

<a id="org855daf1"></a>

### `map` and `filter`

    l = ["abc", "cde", "efg", "fgh", "aaa"]
    def has_a(str):
        if any([c == "a" for c in str]):
            return str
    # map(has_a, l)
    print("Map:")
    print(list(map(has_a,l)))
    # for x in map(has_a, l):
    #     print(x)

    print("Filter:")
    print(list(filter(has_a,l)))
    # for x in filter(has_a, l):
    #     print(x)

    print([x for x in l if has_a(x)])

    a = [[96], [69]]

    print(''.join(list(map(str, a))))
    print(type(''.join(list(map(str, a)))))

<a id="orge2fe286"></a>

### Assignment - list comprehension

    # Input data: List of dictionaries
    employee_list = [
       {"id": 12345, "name": "John", "department": "Kitchen"},
       {"id": 12456, "name": "Paul", "department": "House Floor"},
       {"id": 12478, "name": "Sarah", "department": "Management"},
       {"id": 12434, "name": "Lisa", "department": "Cold Storage"},
       {"id": 12483, "name": "Ryan", "department": "Inventory Mgmt"},
       {"id": 12419, "name": "Gill", "department": "Cashier"}
    ]

    # Function to be passed to the map() function. Do not change this.
    def mod(employee_list):
       temp = employee_list['name'] + "_" + employee_list["department"]
       return temp

    def to_mod_list(employee_list):
       """ Modifies the employee list of dictionaries into list of employee-department strings

       [IMPLEMENT ME]
          1. Use the map() method to apply mod() to all elements in employee_list

       Args:
          employee_list: list of employee objects

       Returns:
          list - A list of strings consisting of name + department.
       """
       ### WRITE SOLUTION CODE HERE
       return list(map(mod, employee_list))
       #raise NotImplementedError()

    def generate_usernames(mod_list):
       """ Generates a list of usernames

       [IMPLEMENT ME]
          1. Use list comprehension and the replace() function to replace space
             characters with underscores

          List comprehension looks like:
          list = [ function() for <item> in <list> ]

          The format for the replace() function is:

          test_str.replace(“a”, “z”) # replaces every “a” in test_str with “z”

       Args:
          mod_list: list of employee-department strings

       Returns:
          list - A list of usernames consisting of name + department delimited by underscores.
       """
       return [str.replace(" ", "_") for str in mod_list]
       ### WRITE SOLUTION CODE HERE

       #raise NotImplementedError()

    def map_id_to_initial(employee_list):
       """ Maps employee id to first initial

       [IMPLEMENT ME]
          1. Use dictionary comprehension to map each employee's id (value) to the first letter in their name (key)

          Dictionary comprehension looks like:
          dict = { key : value for <item> in <list> }

       Args:
          employee_list: list of employee objects

       Returns:
          dict - A dictionary mapping an employee's id (value) to their first initial (key).
       """
       #return {value:key for (key,value) in employ.items() for employ in employee_list}
       ids=[]
       names=[]
       for d in employee_list:
           ids.append(d["id"])
           names.append(str(d["name"])[0])
       return {value:key for (key, value) in zip(ids, names)}

       ### WRITE SOLUTION CODE HERE

       #raise NotImplementedError()

    def main():
       mod_emp_list = to_mod_list(employee_list)
       print("Modified employee list: " + str(mod_emp_list) + "\n")

       print(f"List of usernames: {generate_usernames(mod_emp_list)}\n")

       print(f"Initials and ids: {map_id_to_initial(employee_list)}")

    if __name__ == "__main__":
       main()

<a id="org238d64a"></a>

### Object Oriented Programing (OOP)

Structure:

- Classes;
- Objects;
- Methods.

1.  Classes

    Logical code-block with `attributes` and `behavior`.

    - `Classes` are defined using the key-word `class`;
    - `Attributes` can be `variables`;
    - `Behavior` can be `functions`.

2.  Objects

    `Objects` are instances of `Classes`.

        Bundle, to the *class* =employee=, the attributes =position= and =employment_status=

3.  OOP in Python

    > You previously encountered the four main pillars of object oriented programming. These are: **encapsulation, polymorphism, inheritance and abstraction**

4.  Istantiation process

    - Class definition;
    - New Instance;
    - Initializing new instance.

5.  Attribute References

    To access data defined inside the class scope.

6.  Examples

        class MyClass():
            a = 5
            print("Hello")

        myc = MyClass()
        print(MyClass.a)
        print(myc.a)

        class MyClass():
            a = 5
            def hello(self):
                print("Hello, world!")

        myc = MyClass()
        print(MyClass.a)
        print(myc.hello())
        myc.hello()

        class House:
            '''
            This is a stub for a class representing a house that can be used to create objects and evaluate different metrics that we may require in constructing it.
            '''
            num_rooms = 5
            bathrooms = 2
            def cost_evaluation(self):
                print(self.num_rooms)
                pass
                # Functionality to calculate the costs from the area of the house

        house = House()
        print(house.num_rooms)
        print(House.num_rooms)

        house.num_rooms = 7
        print(house.num_rooms)
        print(House.num_rooms)

        House.num_rooms = 10
        house2 = House()
        print(house2.num_rooms)
        print(House.num_rooms)

7.  Exercise

        class MyFirstClass():
            print("Who wrote this?")
            index = "Author-Book"

            # def __init__(self, index) -> None:
            #     self.index = index

            def hand_list(self, philosopher, book):
                print(MyFirstClass.index)
                print("{} wrote the book: {}".format(philosopher, book))

        whodunnit = MyFirstClass()
        whodunnit.hand_list("Sun Tzu", "The Art of War")

        class A:
            print("Print inside A.")

            def __init__(self, c):
                print("---------Inside class A----------")
                self.c = c

            def alpha(self):
                c = self.c + 1
                return c


        print(dir(A))
        print("Instantiating A..")
        # a = A(1)
        # print(a.alpha())


        class B:
            def __init__(self, a):
                print("---------Inside class B----------")
                self.a = a
            # print(a.alpha())
            d = 5
            print(d)
            # print(a)

        print("Instantiating B..")
        # b = B(a)
        # print(a)

<a id="orgde094ec"></a>

### Extra resources

The following resources will be helpful as additional references in dealing with different concepts related to the topics you have covered in this module.

Programming styles in Python
<https://newrelic.com/blog/nerd-life/python-programming-styles>

Different types of algorithms used in Python
<https://www.thetechplatform.com/post/different-types-of-algorithms-in-data-structure>

Introduction to Big-O notation
<https://dev.to/sarah_chima/the-big-o-notation-an-introduction-34f7>

---

The following resources will be helpful as additional references in dealing with different concepts related to the topics you have covered in this lesson.

OOP Principles
<https://www.geeksforgeeks.org/python-oops-concepts/>

In-depth understanding of MRO
<https://www.python.org/download/releases/2.3/mro/>

OOP Principles/ Classes and objects
<https://realpython.com/python3-object-oriented-programming/>

<a id="org507c361"></a>

## Week4-notes - Modules, Packages, Libraries and Testing

<a id="orgbc4b7ec"></a>

### Imports

- Only loaded once;
- Can be loaded, only inside a scope;

  import sys

  loc = sys.path
  for i in loc:
  print(i)

  import calendar

  leapdays = calendar.leapdays(2000, 2050)
  print(leapdays)

<a id="orga4c038b"></a>

### Scopes

1.  Intro and types of scopes in python

    The scopes in python are classified as:

    - `local`;
    - `enclosed`;
    - `global`;
    - `built-in`;

2.  Scope resolution

    - LEGB rule
    - **Local**: inside funtion;
    - Enclosed: inside enclosed or nested function;
    - **Global**: upmost level, outside functions;
    - Built-in: in the built-in modules;

      globals() # built-in function
      locals() # built-in function

<a id="org77ac697"></a>

### Additional Resource

Learn more
Here is a list of resources that may be helpful as you continue your learning journey.

How To Import Modules in Python 3 (Digital Ocean)

Import modules in Python
<https://www.digitalocean.com/community/tutorials/how-to-import-modules-in-python-3>

Python Modules (Programiz)
<https://www.programiz.com/python-programming/modules>

Python Packages (Real Python)
<https://realpython.com/python-modules-packages/#python-packages>

<a id="orgc8364eb"></a>

### Most common libraries

- OS
- SYS
- CSV
- JSON
- importlib
- re
- math
- intertools

1.  Data Science

    - numpy
    - scipy
    - nltk
    - pandas

2.  Image processing and Visualization

    - OpenCV
    - matplotlib

3.  ML and AI

    - Tensorflow
    - PyTorch
    - Keras

    Others common:

    - SciPy
    - Scikit-learn
    - Theano

4.  **Web Development**

    - Flask: Micro-Framework
    - Django: Full-stack

    Others common:

    - cherry pie
    - pyramid
    - beatiful soup
    - selenium

<a id="orgeddca00"></a>

### Examples of libraries-use

1.  Pandas

        import pandas as pd

        a = pd.DataFrame(
            {
                "Animals": ["Dog", "Cat", "Lion", "Cow", "Elephant"],
                "Sounds": ["Barks", "Meow", "Roars", "Moo", "Trumpet"],
            }
        )

        print(a)
        print(a.describe())

        b = pd.DataFrame(
            {"Letters": ["a", "b", "c", "d", "e", "f"], "Numbers": [12, 7, 9, 3, 5, 1]}
        )

        print(b.sort_values(by="Numbers"))

        b = b.assign(new_values=b["Numbers"] * 3).sort_values(by="Numbers")
        print(b)

2.  NLTK

        import nltk

        text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."
        from nltk.tokenize import word_tokenize
        from nltk.corpus import stopwords

        # Print statement 1
        print(word_tokenize(text))
        # Print statement 2
        print(nltk.tokenize.sent_tokenize(text))


        stopwords = stopwords.words("english")
        new_text = []
        for i in text.split():
            if i not in stopwords:
                new_text.append(i)

        # Print statement 3
        print(new_text)

<a id="org2282ad8"></a>

### More on Big Data and Analysis in Python

> Big Data and Analysis with Python
> With the advent of social media and its widespread acceptance came the unprecedented need for data management. Now billions of gigabytes of data are produced every day and much of it is generated by the end-users. Organizations recognized the huge potential in harnessing this data using predictive and machine learning algorithms to generate insights. But before tackling that challenge, came the challenge of efficiently and systematically storing and handling this data in a way that made it available for quick access.
>
> Big data is the management of large sets of data, both structured and unstructured. Today, this large amount of data is stored in the form of data warehouses and data lakes, both on servers and in the cloud. The main characteristics that are commonly identified for use of Big Data tools are Volume, Variability and Velocity.
>
> Volume is the size of data under question and, if large enough, may require different handling to traditional data storage and management.
>
> Variability or veracity refers to the inconsistency that may be present in this data. In huge data repositories, it is difficult to intervene manually on every wrong entry and thus enough scope for variability must be defined and established while handling such data.
>
> Velocity is the speed of handling this data. With data sources such as social media which are continually active, there is a need for constant updates as well as robust storage. When there is a need to be processed, it should also not create a bottleneck where data retrieval takes longer. As such, velocity plays a very important role in Big Data.
>
> This is the ability to handle a large amount of heterogeneous data with ease of access and speedy processing. The next step in this process is when this data is analyzed and is broadly called data analysis. The final step is publishing this data in form of reports, visualizations and web pages, as per the requirement.
>
> The whole pipeline can be summarized as below:
>
> Big Data Order of Operations Procedural sequence of actions in big data
> Here are several reasons why Python has found a place in the domain of Big Data:
>
> Ease of use: Ease of use is a prerequisite for any large-scale and commonly used technology and language. Python helps setting up and running infrastructure with just a few lines of code.
>
> Licensing structure and open-source nature: The open source paradigm has picked up immensely in recent years. Python provides many very well developed open-source libraries and frameworks, even for large scale applications. Some organizations prefer this, as it saves on cost, as well as providing easier licensing.
>
> Active community: The Python community today is vast and very supportive. This helps with the swift resolution of issues a user may face, as well as the development of new features when required.
>
> Libraries: Possibly the strongest reason for the acceptance of Python is the host of libraries that provide direct support for Big Data. In addition, there are many packages that also aid in bridging the gap between Python and other languages and tools enabling swift deployment of services.
>
> High compatibility with Hadoop and Spark: Hadoop and its Hadoop distributed file system is arguably one of the best solutions for large-scale storage. The support available in Python has also helped in wider acceptance of Python. The same can be said about Spark as Python has supportive libraries such as PySpark and host of API libraries that facilitate its usage.
>
> High processing speed: Python has support for prototyping and with its Object-oriented methodology, processing in Python is much better in comparison to other languages. With its increase in speed, Python is also able to provide adequate stability in its usage.
>
> Portability and scalability: Broadly as mentioned before, Python’s support for cross-language platforms and operations, its ease of extensibility, various libraries, support for frameworks and API overall, makes it easy to scale and flexible.
>
> Python tools and libraries: Most of the libraries in Python that are used for Big Data are widely common and is associate with Data Sciences and Machine Learning. Big Data includes wide-scale usage and acceptance of libraries such as: Numpy, Pandas, Scikit-learn and Scipy. To name just a few.
>
> Additionally, here are a few more libraries that are more specific to a Big Data domain such as:
>
> RedShift and S3: Amazon services are used with their cloud services. S3 is a storage service and RedShift is a data warehousing service.
>
> BigQuery: Developed by Google, BigQuery is a Cloud service library that is useful with RESTful APIs.
>
> PySpark: This is an open-source framework used for large scale data processing and works with resilient distributed datasets.
>
> Kafka: This is a publish-subscribe messaging system that receives logs in the form of packages and is stored in partitioned spaces.
>
> Pydoop: Pydoop provides an interface between Hadoop and Python and support for handling its Hadoop distributed file systems.

<a id="orgc81e020"></a>

### Web Frameworks

- Full-stack
- Microframeworks
- Asynchonous

1.  Full-stack

    Offers things such as:

    - Form generators
    - Template layouts
    - HTTP request handling
    - WSGI interfaces
    - Database connection handling

    **Most common frameworks:**

    - Django
    - Web2py
    - Pyramid

2.  Microframworks

    Do not offer as much patterns and functionalities.
    Used in smaller webprojects and building APIs.

    - Flask
    - Bottle
    - Dash
    - CherryPi

3.  Asynchronous

    Used to handle large amounts of connections.

    - Growler
    - AIOHTTP
    - Sanic

4.  Factors to consider, when choosing framework

    - Available documentation
    - Scalability
    - Flexibility
    - Integration

<a id="orgf2720d8"></a>

### Additional Resources

The following resources will be helpful as additional references in dealing with different concepts related to the topics you have covered in this module:

Popular packages in Python
<https://www.netsolutions.com/insights/top-10-python-frameworks-for-web-development-in-2019/>
Popular Python packages for web development
<https://www.netsolutions.com/insights/top-10-python-frameworks-for-web-development-in-2019/>
ML and AI libraries in Python
<https://towardsdatascience.com/best-python-libraries-for-machine-learning-and-deep-learning-b0bd40c7e8c>
Data Science libraries in Python
<https://www.dataquest.io/blog/15-python-libraries-for-data-science/>

<a id="org2ba6af2"></a>

### Features of using libraries for testing

Solve:

- Bugs quickly
- Gaps
- Defects
- Missing requirements

Helps with:

- Poor design
- Functionalities
- Scalability
- Security
- AB testing
- Compatibility
- Assurance
- Experience

<a id="org2313c48"></a>

### What `testing` must have

- Re-usability
- Traceability
- Efficiency

<a id="org6334af5"></a>

### Testing Life Cycle

- Planning
- Preparation
- Execution
- Reporting

The steps to achieve this can include:

- Writing scripts to test cases
- Compile tests results
- Correct defects based on them
- Generating reports from tests

<a id="org64488c1"></a>

### Good testing leads to

- Great bug coverage
- Re-usability of code
- Better user experience
- Reduce costs
- Increase satisfaction

<a id="org97d4e25"></a>

### Types of testing

Broadly can be categorized by:

- White box (accessible source code)
- Black box (not accessible source code)

Types:

- Compatibility testing
- Ad hoc
- Usability
- Regression testing

<a id="orgb7930c8"></a>

### How to know there was sufficient testing

- Amount of test cycles
- Passing percentage
- Deadlines
- Time intervals

<a id="org0b82843"></a>

### Deep-in types of testing

**Levels of testing**:

- Unit
- Integration
- System
- Acceptance

OBS.:
Other ways to categorize testing:

- Functional tests
- Non-functional tests
- Maintenance test

1.  Functional tests

    Tests if the output is compliant with what was requested/expected.

2.  Non-functional test

    Based on metrics on overall performance and quality.

3.  Maintenance test

    When the underlining system and it&rsquo;s operations and environments are corrected, changed or extended.

<a id="orgea0499b"></a>

### Levels of testing

The levels of testing are sequential and build on each other.

1.  Unit testing

    Designed for individual components, by isolating them.

    Components are low-level (close to the level of the written code).

    Usually involve use automation for `continuous integration` (CI), given their small sizes.

    So, tests can be written, while writting the code.

    1.  Example

        Using `pytest` to test components, in Python.

2.  Integration test

    Test how one component affect the other, and the flow of information between them.

    Key-word: **Interface**.

    Different approaches, depending on unit tests:

    - Top-down
    - Bottom-up
    - Sandwich

    1.  Example

        Test if data is correctly fetched from a `database`. Then, send it to the webpage.

3.  System testing

    Test the performance of the application as-a-whole. Test software against the requirements, to assure completeness.

    Includes measurement of the location of deployment of the application and components. So to assure that the app has:

    - Reliability;
    - Performance;
    - Security;
    - Load balancing.
    - Operability of the platform and OS.

    **OBS.: most important stage in a team of testers. And, it&rsquo;s the most critical, because it&rsquo;s the final stage, before deployment for end-users.**

4.  Acceptance testing

    When code arrives at this stage, it&rsquo;s expected to be ready for deploymeny, and bug-free, as well as compliant to the imposed standards.

    - Alpha.
    - Beta.
    - Regression testing.

    Involves stack-holders and end-users.

    Use pre-written scenarios and try to find bugs.

5.  Final words

    The key for testing is: frequent testing and early. While each of the steps are important, early testing saves time, effort and money.

    As code gets larger, they become harder to fix.

<a id="orgd5b24c1"></a>

### Testing in Python

Generally involved in:

- Prepare the test environment
- Run the test scripts
- Analyze the results

1.  `Unittest` framework

    Built-in testing package.

    Supports:

    - Automation testing
    - Independent testing modules
    - Aggregation

2.  `Pytest`

    Supports:

    - Functional test-types:
      - Unit
      - Integration
      - End-to-end
    - Parameterized test-types:
      - Enables execution tests multiple times, with different parameters passed.
    - Parallel test-types:
      - Generate HTML, XML or plain text reports
    - Integration with different `test frameworks`
      - Pyunit
      - Nose
      - Flask
      - Django

    Can test:

    - APIs
    - UI
    - Database connections
    - Other web-applications.

3.  Robot

    > Keyword-driven development capabilities

    Key-words can be pre-defined or user-defined

    Used for acceptance testing, Robotic Process Automation (RPA), Test-Driven Development (TDD).

    Can be used for:

    - Android
    - APIs
    - Mainframes

4.  Selenium

    Mostly for web-applications

    Browser and OS support.

    Browser-specific web drivers:

    - Logins
    - Buttons
    - Form-filling

<a id="orgec18445"></a>

### Pytest testing

    def add(a,b):
        return a+b

    def sub(a,b):
        return a-b

    import addition
    import pytest

    def test_add():
        assert addition.add(4,5) == 9

    def test_sub():
        assert addition.sub(4,5) == -1

In the terminal,

    pytest test_addition.py

Or, to test only one function,

    pytest test_addition.py::test_add

<a id="org1f68493"></a>

### TDD (Test-Driven Development)

Write test, before writting the code for a feature, app etc.

[![img](./img/TDD.png)](img/TDD.png)

OBS.: step 5: rerun the process.

This **process** is also called the `red-green refactor cycle`.

[![img](./img/red-green-cycle.png)](img/red-green-cycle.png)

1.  Positives

    - Write tests **first**.
    - Makes sure **application** is **compliant to tests**.
    - Predicable behavior, from start.
    - Easier to integrate components, later.
    - Ease to refactor, in need of changes.

<a id="orgf7fb4ac"></a>

### Other types of development cycles

- Behavior-driven
- Acceptance-driven
- Scaling-driven
- Developer-test-driven

<a id="org610139f"></a>

### Examples TDD

    from curses.ascii import isdigit
    import findstring
    import pytest

    def test_ispresent():
        assert findstring.ispresent("Al")

    def test_nodigit():
        assert map(lambda p: findstring.nodigit(p), findstring.names)

    names = ["Al", "Bo", "Chi", "Ma"]
    def ispresent(person):
        if person in names:
            return True
        else:
            return False

    def nodigit(person):
        if person.isaplha():
            return True
        else:
            return False

<a id="org130ad09"></a>

### Additional Resources

The following resources will be helpful as additional references in dealing with different concepts related to the topics we have covered in this module.

Test-Driven Development
<https://testdriven.io/blog/modern-tdd/>
Test-driven Development with PyTest
<https://stackabuse.com/test-driven-development-with-pytest/>
PyTest Official website
<https://docs.pytest.org/en/7.1.x/>
Test automation packages in Python
<https://www.geeksforgeeks.org/best-python-modules-for-automation/>

<a id="orge9d965d"></a>

### Final Test

    for x in range(1, 4):
        print(int((str((float(x))))))

    str = 'Pomodoro'
    for l in str:
    if l == 'o':
        str = str.split()
        print(str, end=", ")

    def d():
        color = "green"
        def e():
            nonlocal color
            color = "yellow"
        e()
        print("Color: " + color)
        color = "red"
    color = "blue"
    d()

    num = 9
    class Car:
        num = 5
        bathrooms = 2

    def cost_evaluation(num):
        num = 10
        return num

    class Bike():
        num = 11

    cost_evaluation(num)
    car = Car()
    bike = Bike()
    car.num = 7
    Car.num = 2
    print(num)

    Class P():
        pass
    Class C(P):
        pass
    p=P()
    c=C()
    # print(issubclass(p,P))
    # print(issubclass(C,c))
    print(issubclass(C,P))
    # print(issubclass(C,P))

    class A:
       def a(self):
           return "Function inside A"

    class B:
       def a(self):
           return "Function inside B"

    class C:
       pass

    class D(C, A, B):
       pass

    d = D()
    print(d.a())

<a id="org9cc9700"></a>

# Version Control
