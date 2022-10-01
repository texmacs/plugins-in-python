<TeXmacs|2.1.3>

<style|<tuple|generic|british|doc>>

<\body>
  <doc-data|<doc-title|001: Re-impl the Graphviz
  plugin>|<doc-author|<author-data|<author-name|Da>>>>

  <section|Description>

  Re-implement the Graphviz plugin implemented in Python to this repo.

  Here is the list of re-lated files:

  <\itemize>
    <item><slink|https://gitee.com/texmacs/texmacs/blob/v2.1.2/plugins/tmpy/session/tm_graphviz.py>

    <item><slink|https://gitee.com/texmacs/texmacs/tree/v2.1.2/plugins/graphviz>
  </itemize>

  <section|How to test it?>

  <\shell-code>
    ./pants run cli:install -- graphviz
  </shell-code>

  Launch it and test it via <menu|Help|Plugins|Graphviz>.

  <section|How much time did you spend on it?>

  <\itemize>
    <item>Start time: 2022/10/01 08:30:00 UTC+8

    <item>End time: 2022/10/01 09:13:00 UTC+8
  </itemize>

  About 45 minutes.
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
    <associate|auto-3|<tuple|2|1>>
    <associate|auto-4|<tuple|3|?>>
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

      <vspace*|1fn><with|font-series|<quote|bold>|math-font-series|<quote|bold>|3<space|2spc>How
      much time did you spend on it?> <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-3><vspace|0.5fn>
    </associate>
  </collection>
</auxiliary>