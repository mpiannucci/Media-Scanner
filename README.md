Media-Scanner
=============

Python media scanner

A post download script used in conjunction with the transmission-daemon bittorent client.

<h2>Dependencies</h2>
<ul>
  <li>Python 2.7</li>
  <li>transmissionrpc python module
    <code>sudo easy_install transmissionrpc</code>
  </li>
  <li>transmission-daemon
    <code>sudo apt-get install transmission-daemon</code>
  </li>
  <li>xbmc tools
    <code>sudo apt-get install xbmc-eventclients-xbmc-send</code>
  </li>
</ul>

<h2>Instructions</h2>
<ul>
  <li>Download the transmission-daemon <code>sudo apt-get install transmission-daemon</code></li>
  <li>Stop the service <code>sudo service transmission-daemon stop</code></li>
  <li>Modify the init.d script to run the program as root.</li>
  <li>Set the configuration for the web and rpc interfaces</li>
  <li>Set the download folder and remember its path</li>
  <li>Set script-on-finish to true and the path to TorrentFinished as the file location</li>
  <li>Restart the service <code>sudo service transmission-daemon start</code></li>
  <li>Set variables in scanner.py script as they apply to you <code>cp scanner.cfg.exampl scanner.cfg</code></li>
  <li>Added a torrect via rpc or web interface and test!</li>
</ul>
  
