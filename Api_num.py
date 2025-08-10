<!doctype html><html><head><title>Editorial Preview</title></head><body><p>html&gt;<head><title>Editorial Preview</title></head><body><p>.. _installing-packages:</p></p>

<h1></h1>
 

<h1>Installing Packages</h1>
 

<p>This section covers the basics of how to install Python :term:<code>packages
<Distribution Package></code>.</p>
 

<p>It&rsquo;s important to note that the term “package” in this context is being used to
describe a bundle of software to be installed (i.e. as a synonym for a
:term:<code>distribution <Distribution Package></code>). It does not refer to the kind
of :term:<code>package <Import Package></code> that you import in your Python source code
(i.e. a container of modules). It is common in the Python community to refer to
a :term:<code>distribution <Distribution Package></code> using the term “package”.  Using
the term “distribution” is often not preferred, because it can easily be
confused with a Linux distribution, or another larger software distribution
like Python itself.</p>
 

<p>.. <em>installing</em>requirements:</p>
 

<h1>Requirements for Installing Packages</h1>
 

<p>This section describes the steps to follow before installing other Python
packages.</p>
 

<h2>Ensure you can run Python from the command line</h2>
 

<p>Before you go any further, make sure you have Python and that the expected
version is available from your command line. You can check this by running:</p>
 

<p>.. tab:: Unix/macOS</p>
 

<pre><code>.. code-block:: bash
 
    python3 --version
</code></pre>
 

<p>.. tab:: Windows</p>
 

<pre><code>.. code-block:: bat
 
    py --version
</code></pre>
 

<p>You should get some output like <code>Python 3.6.3</code>. If you do not have Python,
please install the latest 3.x version from <code>python.org</code>_ or refer to the
:ref:<code>Installing Python <python-guide:installation></code> section of the Hitchhiker&rsquo;s Guide to Python.</p>
 

<p>.. Note:: If you&rsquo;re a newcomer and you get an error like this:</p>
 

<pre><code>.. code-block:: pycon
 
    >>> python3 --version
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'python3' is not defined
 
It's because this command and other suggested commands in this tutorial
are intended to be run in a *shell* (also called a *terminal* or
*console*). See the Python for Beginners `getting started tutorial`_ for
an introduction to using your operating system's shell and interacting with
Python.
</code></pre>
 

<p>.. Note:: If you&rsquo;re using an enhanced shell like IPython or the Jupyter
   notebook, you can run system commands like those in this tutorial by
   prefacing them with a <code>!</code> character:</p>
 

<p>.. code-block:: text</p>
 

<pre><code>    In [1]: import sys
            !{sys.executable} --version
    Python 3.6.3
</code></pre>
 

<p>It&rsquo;s recommended to write <code>{sys.executable}</code> rather than plain <code>python</code> in
   order to ensure that commands are run in the Python installation matching
   the currently running notebook (which may not be the same Python
   installation that the <code>python</code> command refers to).</p>
 

<p>.. Note:: Due to the way most Linux distributions are handling the Python 3
   migration, Linux users using the system Python without creating a virtual
   environment first should replace the <code>python</code> command in this tutorial
   with <code>python3</code> and the <code>python -m pip</code> command with <code>python3 -m pip --user</code>. Do <em>not</em>
   run any of the commands in this tutorial with <code>sudo</code>: if you get a
   permissions error, come back to the section on creating virtual environments,
   set one up, and then continue with the tutorial as written.</p>
 

<p>.. <em>getting started tutorial: <a href="https://opentechschool.github.io/python-beginners/en/getting">https://opentechschool.github.io/python-beginners/en/getting</a></em>started.html#what-is-python-exactly
.. _python.org: <a href="https://www.python.org">https://www.python.org</a></p>
 

<h2>Ensure you can run pip from the command line</h2>
 

<p>Additionally, you&rsquo;ll need to make sure you have :ref:<code>pip</code> available. You can
check this by running:</p>
 

<p>.. tab:: Unix/macOS</p>
 

<pre><code>.. code-block:: bash
 
    python3 -m pip --version
</code></pre>
 

<p>.. tab:: Windows</p>
 

<pre><code>.. code-block:: bat
 
    py -m pip --version
</code></pre>
 

<p>If you installed Python from source, with an installer from <code>python.org</code><em>, or
via <code>Homebrew</code></em> you should already have pip. If you&rsquo;re on Linux and installed
using your OS package manager, you may have to install pip separately, see
:doc:<code>/guides/installing-using-linux-tools</code>.</p>
 

<p>.. _Homebrew: <a href="https://brew.sh">https://brew.sh</a></p>
 

<p>If <code>pip</code> isn&rsquo;t already installed, then first try to bootstrap it from the
standard library:</p>
 

<p>.. tab:: Unix/macOS</p>
 

<pre><code>.. code-block:: bash
 
    python3 -m ensurepip --default-pip
</code></pre>
 

<p>.. tab:: Windows</p>
 

<pre><code>.. code-block:: bat
 
    py -m ensurepip --default-pip
</code></pre>
 

<p>If that still doesn&rsquo;t allow you to run <code>python -m pip</code>:</p>
 

<ul>
<li><p>Securely Download <code>get-pip.py
<https://bootstrap.pypa.io/get-pip.py></code>_ [1]_</p></li>
<li><p>Run <code>python get-pip.py</code>. [2]_  This will install or upgrade pip.
Additionally, it will install :ref:<code>setuptools</code> and :ref:<code>wheel</code> if they&rsquo;re
not installed already.</p>
 
<p>.. warning::</p>
 
<p>Be cautious if you&rsquo;re using a Python install that&rsquo;s managed by your
 operating system or another package manager. get-pip.py does not
 coordinate with those tools, and may leave your system in an
 inconsistent state. You can use <code>python get-pip.py --prefix=/usr/local/</code>
 to install in <code>/usr/local</code> which is designed for locally-installed
 software.</p></li>
</ul>
 

<h2>Ensure pip, setuptools, and wheel are up to date</h2>
 

<p>While <code>pip</code> alone is sufficient to install from pre-built binary archives,
up to date copies of the <code>setuptools</code> and <code>wheel</code> projects are useful
to ensure you can also install from source archives:</p>
 

<p>.. tab:: Unix/macOS</p>
 

<pre><code>.. code-block:: bash
 
    python3 -m pip install --upgrade pip setuptools wheel
</code></pre>
 

<p>.. tab:: Windows</p>
 

<pre><code>.. code-block:: bat
 
    py -m pip install --upgrade pip setuptools wheel
</code></pre>
 

<h2>Optionally, create a virtual environment</h2>
 

<p>See :ref:<code>section below <Creating and using Virtual Environments></code> for details,
but here&rsquo;s the basic :doc:<code>venv <python:library/venv></code> [3]_ command to use on a typical Linux system:</p>
 

<p>.. tab:: Unix/macOS</p>
 

<pre><code>.. code-block:: bash
 
    python3 -m venv tutorial_env
    source tutorial_env/bin/activate
</code></pre>
 

<p>.. tab:: Windows</p>
 

<pre><code>.. code-block:: bat
 
    py -m venv tutorial_env
    tutorial_env\Scripts\activate
</code></pre>
 

<p>This will create a new virtual environment in the <code>tutorial_env</code> subdirectory,
and configure the current shell to use it as the default <code>python</code> environment.</p>
 

<p>.. _Creating and using Virtual Environments:</p>
 

<h1>Creating Virtual Environments</h1>
 

<p>Python “Virtual Environments” allow Python :term:<code>packages <Distribution
Package></code> to be installed in an isolated location for a particular application,
rather than being installed globally. If you are looking to safely install
global command line tools,
see :doc:<code>/guides/installing-stand-alone-command-line-tools</code>.</p>
 

<p>Imagine you have an application that needs version 1 of LibFoo, but another
application requires version 2. How can you use both these applications? If you
install everything into /usr/lib/python3.6/site-packages (or whatever your
platformâ€™s standard location is), itâ€™s easy to end up in a situation where you
unintentionally upgrade an application that shouldnâ€™t be upgraded.</p>
 

<p>Or more generally, what if you want to install an application and leave it be?
If an application works, any change in its libraries or the versions of those
libraries can break the application.</p>
 

<p>Also, what if you canâ€™t install :term:<code>packages <Distribution Package></code> into the
global site-packages directory? For instance, on a shared host.</p>
 

<p>In all these cases, virtual environments can help you. They have their own
installation directories and they donâ€™t share libraries with other virtual
environments.</p>
 

<p>Currently, there are two common tools for creating Python virtual environments:</p>
 

<ul>
<li>:doc:<code>venv <python:library/venv></code> is available by default in Python 3.3 and later, and installs
:ref:<code>pip</code> into created virtual environments in Python 3.4 and later
(Python versions prior to 3.12 also installed :ref:<code>setuptools</code>).</li>
<li>:ref:<code>virtualenv</code> needs to be installed separately, but supports Python 2.7+
and Python 3.3+, and :ref:<code>pip</code>, :ref:<code>setuptools</code> and :ref:<code>wheel</code> are
installed into created virtual environments by default. Note that <code>setuptools</code> is no longer
included by default starting with Python 3.12 (and <code>virtualenv</code> follows this behavior).</li>
</ul>
 

<p>The basic usage is like so:</p>
 

<p>Using :doc:<code>venv <python:library/venv></code>:</p>
 

<p>.. tab:: Unix/macOS</p>
 

<pre><code>.. code-block:: bash
 
    python3 -m venv <DIR>
    source <DIR>/bin/activate
</code></pre>
 

<p>.. tab:: Windows</p>
 

<pre><code>.. code-block:: bat
 
    py -m venv <DIR>
    <DIR>\Scripts\activate
</code></pre>
 

<p>Using :ref:<code>virtualenv</code>:</p>
 

<p>.. tab:: Unix/macOS</p>
 

<pre><code>.. code-block:: bash
 
    python3 -m virtualenv <DIR>
    source <DIR>/bin/activate
</code></pre>
 

<p>.. tab:: Windows</p>
 

<pre><code>.. code-block:: bat
 
    virtualenv <DIR>
    <DIR>\Scripts\activate
</code></pre>
 

<p>For more information, see the :doc:<code>venv <python:library/venv></code> docs or
the :doc:<code>virtualenv <virtualenv:index></code> docs.</p>
 

<p>The use of :command:<code>source</code> under Unix shells ensures
that the virtual environment&rsquo;s variables are set within the current
shell, and not in a subprocess (which then disappears, having no
useful effect).</p>
 

<p>In both of the above cases, Windows users should <em>not</em> use the
:command:<code>source</code> command, but should rather run the :command:<code>activate</code>
script directly from the command shell like so:</p>
 

<p>.. code-block:: bat</p>
 

<p></p><dir>\Scripts\activate<p></p>
 

<p>Managing multiple virtual environments directly can become tedious, so the
:ref:<code>dependency management tutorial <managing-dependencies></code> introduces a
higher level tool, :ref:<code>Pipenv</code>, that automatically manages a separate
virtual environment for each project and application that you work on.</p>
 

<h1>Use pip for Installing</h1>
 

<p>:ref:<code>pip</code> is the recommended installer.  Below, we&rsquo;ll cover the most common
usage scenarios. For more detail, see the :doc:<code>pip docs <pip:index></code>,
which includes a complete :doc:<code>Reference Guide <pip:cli/index></code>.</p>
 

<h1>Installing from PyPI</h1>
 

<p>The most common usage of :ref:<code>pip</code> is to install from the :term:<code>Python Package
Index <Python Package Index (PyPI)></code> using a :term:<code>requirement specifier
<Requirement Specifier></code>. Generally speaking, a requirement specifier is
composed of a project name followed by an optional :term:<code>version specifier
<Version Specifier></code>.  A full description of the supported specifiers can be
found in the :ref:<code>Version specifier specification <version-specifiers></code>.
Below are some examples.</p>
 

<p>To install the latest version of “SomeProject”:</p>
 

<p>.. tab:: Unix/macOS</p>
 

<pre><code>.. code-block:: bash
 
    python3 -m pip install "SomeProject"
</code></pre>
 

<p>.. tab:: Windows</p>
 

<pre><code>.. code-block:: bat
 
    py -m pip install "SomeProject"
</code></pre>
 

<p>To install a specific version:</p>
 

<p>.. tab:: Unix/macOS</p>
 

<pre><code>.. code-block:: bash
 
    python3 -m pip install "SomeProject==1.4"
</code></pre>
 

<p>.. tab:: Windows</p>
 

<pre><code>.. code-block:: bat
 
    py -m pip install "SomeProject==1.4"
</code></pre>
 

<p>To install greater than or equal to one version and less than another:</p>
 

<p>.. tab:: Unix/macOS</p>
 

<pre><code>.. code-block:: bash
 
    python3 -m pip install "SomeProject>=1,<2"
</code></pre>
 

<p>.. tab:: Windows</p>
 

<pre><code>.. code-block:: bat
 
    py -m pip install "SomeProject>=1,<2"
</code></pre>
 

<p>To install a version that&rsquo;s :ref:<code>compatible <version-specifiers-compatible-release></code>
with a certain version: [4]_</p>
 

<p>.. tab:: Unix/macOS</p>
 

<pre><code>.. code-block:: bash
 
    python3 -m pip install "SomeProject~=1.4.2"
</code></pre>
 

<p>.. tab:: Windows</p>
 

<pre><code>.. code-block:: bat
 
    py -m pip install "SomeProject~=1.4.2"
</code></pre>
 

<p>In this case, this means to install any version “==1.4.*” version that&rsquo;s also
“>=1.4.2”.</p>
 

<h1>Source Distributions vs Wheels</h1>
 

<p>:ref:<code>pip</code> can install from either :term:<code>Source Distributions (sdist) <Source
Distribution (or "sdist")></code> or :term:<code>Wheels <Wheel></code>, but if both are present
on PyPI, pip will prefer a compatible :term:<code>wheel <Wheel></code>. You can override
pip<code>s default behavior by e.g. using its :ref:</code>–no-binary
<a href="pip:install_--no-binary">pip:install_–no-binary</a> option.</p>
 

<p>:term:<code>Wheels <Wheel></code> are a pre-built :term:<code>distribution <Distribution
Package></code> format that provides faster installation compared to :term:<code>Source
Distributions (sdist) <Source Distribution (or "sdist")></code>, especially when a
project contains compiled extensions.</p>
 

<p>If :ref:<code>pip</code> does not find a wheel to install, it will locally build a wheel
and cache it for future installs, instead of rebuilding the source distribution
in the future.</p>
 

<h1>Upgrading packages</h1>
 

<p>Upgrade an already installed <code>SomeProject</code> to the latest from PyPI.</p>
 

<p>.. tab:: Unix/macOS</p>
 

<pre><code>.. code-block:: bash
 
    python3 -m pip install --upgrade SomeProject
</code></pre>
 

<p>.. tab:: Windows</p>
 

<pre><code>.. code-block:: bat
 
    py -m pip install --upgrade SomeProject
</code></pre>
 

<p>.. _<code>Installing to the User Site</code>:</p>
 

<h1>Installing to the User Site</h1>
 

<p>To install :term:<code>packages <Distribution Package></code> that are isolated to the
current user, use the <code>--user</code> flag:</p>
 

<p>.. tab:: Unix/macOS</p>
 

<pre><code>.. code-block:: bash
 
    python3 -m pip install --user SomeProject
</code></pre>
 

<p>.. tab:: Windows</p>
 

<pre><code>.. code-block:: bat
 
    py -m pip install --user SomeProject
</code></pre>
 

<p>For more information see the <code>User Installs
<https://pip.pypa.io/en/latest/user_guide/#user-installs></code>_ section
from the pip docs.</p>
 

<p>Note that the <code>--user</code> flag has no effect when inside a virtual environment
- all installation commands will affect the virtual environment.</p>
 

<p>If <code>SomeProject</code> defines any command-line scripts or console entry points,
<code>--user</code> will cause them to be installed inside the <code>user base</code>_&rsquo;s binary
directory, which may or may not already be present in your shell&rsquo;s
:envvar:<code>PATH</code>.  (Starting in version 10, pip displays a warning when
installing any scripts to a directory outside :envvar:<code>PATH</code>.)  If the scripts
are not available in your shell after installation, you&rsquo;ll need to add the
directory to your :envvar:<code>PATH</code>:</p>
 

<ul>
<li><p>On Linux and macOS you can find the user base binary directory by running
<code>python -m site --user-base</code> and adding <code>bin</code> to the end. For example,
this will typically print <code>~/.local</code> (with <code>~</code> expanded to the absolute
path to your home directory) so you&rsquo;ll need to add <code>~/.local/bin</code> to your
<code>PATH</code>.  You can set your <code>PATH</code> permanently by <code>modifying ~/.profile</code>_.</p></li>
<li><p>On Windows you can find the user base binary directory by running <code>py -m
site --user-site</code> and replacing <code>site-packages</code> with <code>Scripts</code>. For
example, this could return
<code>C:\Users\Username\AppData\Roaming\Python36\site-packages</code> so you would
need to set your <code>PATH</code> to include
<code>C:\Users\Username\AppData\Roaming\Python36\Scripts</code>. You can set your user
<code>PATH</code> permanently in the <code>Control Panel</code>_. You may need to log out for the
<code>PATH</code> changes to take effect.</p></li>
</ul>
 

<p>.. <em>user base: <a href="https://docs.python.org/3/library/site.html#site.USER">https://docs.python.org/3/library/site.html#site.USER</a></em>BASE
.. _modifying ~/.profile: <a href="https://stackoverflow.com/a/14638025">https://stackoverflow.com/a/14638025</a>
.. _Control Panel: <a href="https://docs.microsoft.com/en-us/windows/win32/shell/user-environment-variables?redirectedfrom=MSDN">https://docs.microsoft.com/en-us/windows/win32/shell/user-environment-variables?redirectedfrom=MSDN</a></p>
 

<h1>Requirements files</h1>
 

<p>Install a list of requirements specified in a :ref:<code>Requirements File
<pip:Requirements Files></code>.</p>
 

<p>.. tab:: Unix/macOS</p>
 

<pre><code>.. code-block:: bash
 
    python3 -m pip install -r requirements.txt
</code></pre>
 

<p>.. tab:: Windows</p>
 

<pre><code>.. code-block:: bat
 
    py -m pip install -r requirements.txt
</code></pre>
 

<h1>Installing from VCS</h1>
 

<p>Install a project from VCS in “editable” mode.  For a full breakdown of the
syntax, see pip&rsquo;s section on :ref:<code>VCS Support <pip:VCS Support></code>.</p>
 

<p>.. tab:: Unix/macOS</p>
 

<pre><code>.. code-block:: bash
 
    python3 -m pip install -e SomeProject @ git+https://git.repo/some_pkg.git          # from git
    python3 -m pip install -e SomeProject @ hg+https://hg.repo/some_pkg                # from mercurial
    python3 -m pip install -e SomeProject @ svn+svn://svn.repo/some_pkg/trunk/         # from svn
    python3 -m pip install -e SomeProject @ git+https://git.repo/some_pkg.git@feature  # from a branch
</code></pre>
 

<p>.. tab:: Windows</p>
 

<pre><code>.. code-block:: bat
 
    py -m pip install -e SomeProject @ git+https://git.repo/some_pkg.git          # from git
    py -m pip install -e SomeProject @ hg+https://hg.repo/some_pkg                # from mercurial
    py -m pip install -e SomeProject @ svn+svn://svn.repo/some_pkg/trunk/         # from svn
    py -m pip install -e SomeProject @ git+https://git.repo/some_pkg.git@feature  # from a branch
</code></pre>
 

<h1>Installing from other Indexes</h1>
 

<p>Install from an alternate index</p>
 

<p>.. tab:: Unix/macOS</p>
 

<pre><code>.. code-block:: bash
 
    python3 -m pip install --index-url http://my.package.repo/simple/ SomeProject
</code></pre>
 

<p>.. tab:: Windows</p>
 

<pre><code>.. code-block:: bat
 
    py -m pip install --index-url http://my.package.repo/simple/ SomeProject
</code></pre>
 

<p>Search an additional index during install, in addition to :term:<code>PyPI <Python
Package Index (PyPI)></code></p>
 

<p>.. tab:: Unix/macOS</p>
 

<pre><code>.. code-block:: bash
 
    python3 -m pip install --extra-index-url http://my.package.repo/simple SomeProject
</code></pre>
 

<p>.. tab:: Windows</p>
 

<pre><code>.. code-block:: bat
 
    py -m pip install --extra-index-url http://my.package.repo/simple SomeProject
</code></pre>
 

<h1>Installing from a local src tree</h1>
 

<p>Installing from local src in
:doc:<code>Development Mode <setuptools:userguide/development_mode></code>,
i.e. in such a way that the project appears to be installed, but yet is
still editable from the src tree.</p>
 

<p>.. tab:: Unix/macOS</p>
 

<pre><code>.. code-block:: bash
 
    python3 -m pip install -e <path>
</code></pre>
 

<p>.. tab:: Windows</p>
 

<pre><code>.. code-block:: bat
 
    py -m pip install -e <path>
</code></pre>
 

<p>You can also install normally from src</p>
 

<p>.. tab:: Unix/macOS</p>
 

<pre><code>.. code-block:: bash
 
    python3 -m pip install <path>
</code></pre>
 

<p>.. tab:: Windows</p>
 

<pre><code>.. code-block:: bat
 
    py -m pip install <path>
</code></pre>
 

<h1>Installing from local archives</h1>
 

<p>Install a particular source archive file.</p>
 

<p>.. tab:: Unix/macOS</p>
 

<pre><code>.. code-block:: bash
 
    python3 -m pip install ./downloads/SomeProject-1.0.4.tar.gz
</code></pre>
 

<p>.. tab:: Windows</p>
 

<pre><code>.. code-block:: bat
 
    py -m pip install ./downloads/SomeProject-1.0.4.tar.gz
</code></pre>
 

<p>Install from a local directory containing archives (and don&rsquo;t check :term:<code>PyPI
<Python Package Index (PyPI)></code>)</p>
 

<p>.. tab:: Unix/macOS</p>
 

<pre><code>.. code-block:: bash
 
    python3 -m pip install --no-index --find-links=file:///local/dir/ SomeProject
    python3 -m pip install --no-index --find-links=/local/dir/ SomeProject
    python3 -m pip install --no-index --find-links=relative/dir/ SomeProject
</code></pre>
 

<p>.. tab:: Windows</p>
 

<pre><code>.. code-block:: bat
 
    py -m pip install --no-index --find-links=file:///local/dir/ SomeProject
    py -m pip install --no-index --find-links=/local/dir/ SomeProject
    py -m pip install --no-index --find-links=relative/dir/ SomeProject
</code></pre>
 

<h1>Installing from other sources</h1>
 

<p>To install from other data sources (for example Amazon S3 storage)
you can create a helper application that presents the data
in a format compliant with the :ref:<code>simple repository API <simple-repository-api></code>:,
and use the <code>--extra-index-url</code> flag to direct pip to use that index.</p>
 

<p>.. code-block:: bash</p>
 

<p>./s3helper –port=7777
   python -m pip install –extra-index-url http://localhost:7777 SomeProject</p>
 

<h1>Installing Prereleases</h1>
 

<p>Find pre-release and development versions, in addition to stable versions.  By
default, pip only finds stable versions.</p>
 

<p>.. tab:: Unix/macOS</p>
 

<pre><code>.. code-block:: bash
 
    python3 -m pip install --pre SomeProject
</code></pre>
 

<p>.. tab:: Windows</p>
 

<pre><code>.. code-block:: bat
 
    py -m pip install --pre SomeProject
</code></pre>
 

<h1>Installing “Extras”</h1>
 

<p>Extras are optional “variants” of a package, which may include
additional dependencies, and thereby enable additional functionality
from the package.  If you wish to install an extra for a package which
you know publishes one, you can include it in the pip installation command:</p>
 

<p>.. tab:: Unix/macOS</p>
 

<pre><code>.. code-block:: bash
 
    python3 -m pip install 'SomePackage[PDF]'
    python3 -m pip install 'SomePackage[PDF]==3.0'
    python3 -m pip install -e '.[PDF]'  # editable project in current directory
</code></pre>
 

<p>.. tab:: Windows</p>
 

<pre><code>.. code-block:: bat
 
    py -m pip install "SomePackage[PDF]"
    py -m pip install "SomePackage[PDF]==3.0"
    py -m pip install -e ".[PDF]"  # editable project in current directory
</code></pre>
 

<hr>

<p>.. [1] “Secure” in this context means using a modern browser or a
       tool like :command:<code>curl</code> that verifies SSL certificates when
       downloading from https URLs.</p>
 

<p>.. [2] Depending on your platform, this may require root or Administrator
       access. :ref:<code>pip</code> is currently considering changing this by <code>making user
       installs the default behavior
       <https://github.com/pypa/pip/issues/1668></code>_.</p>
 

<p>.. [3] Beginning with Python 3.4, <code>venv</code> (a stdlib alternative to
       :ref:<code>virtualenv</code>) will create virtualenv environments with <code>pip</code>
       pre-installed, thereby making it an equal alternative to
       :ref:<code>virtualenv</code>.</p>
 

<p>.. [4] The compatible release specifier was accepted in :pep:<code>440</code>
       and support was released in :ref:<code>setuptools</code> v8.0 and
       :ref:<code>pip</code> v6.0</p>

<p></dir></body></html></p>
</body></html>