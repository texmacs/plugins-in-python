<TeXmacs|2.1.3>

<style|<tuple|generic|british|doc>>

<\body>
  <doc-data|<doc-title|Re-implement the Python and SymPy
  plugin>|<doc-author|<author-data|<author-name|Da>>>>

  <section|Description>

  SymPy plugin shares the common part with the Python plugin. That's why we
  put then into the same task.

  And we need extra dependencies for the SymPy plugin. Using Pants<\footnote>
    <slink|https://www.pantsbuild.org/docs/python-third-party-dependencies>
  </footnote>, it is very easy to manage Python dependencies, and build a
  PEX<\footnote>
    <slink|https://github.com/pantsbuild/pex>
  </footnote> file for the SymPy plugin.

  <section|How to test it?>

  Install it first:

  <\shell-code>
    ./pants run cli:install -- sympy

    \;

    # For Mogan Editor

    TEXMACS_HOME_PATH=~/.Xmacs ./pants run cli:install -- sympy
  </shell-code>

  Click <menu|Help|Plugins|SymPy> to test it.

  <section|How much time did you spend on it?>

  I have not recorded it, I guess it is about 1 hour.
</body>

<\initial>
  <\collection>
    <associate|page-medium|paper>
  </collection>
</initial>

<\references>
  <\collection>
    <associate|auto-1|<tuple|1|1>>
    <associate|auto-2|<tuple|2|1>>
    <associate|auto-3|<tuple|2|?>>
    <associate|auto-4|<tuple|3|?>>
    <associate|footnote-1|<tuple|1|1>>
    <associate|footnote-2|<tuple|2|1>>
    <associate|footnr-1|<tuple|1|1>>
    <associate|footnr-2|<tuple|2|1>>
  </collection>
</references>

<\auxiliary>
  <\collection>
    <\associate|toc>
      <vspace*|1fn><with|font-series|<quote|bold>|math-font-series|<quote|bold>|1<space|2spc>Description>
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-1><vspace|0.5fn>

      <vspace*|1fn><with|font-series|<quote|bold>|math-font-series|<quote|bold>|2<space|2spc>How
      to test it?> <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-2><vspace|0.5fn>
    </associate>
  </collection>
</auxiliary>