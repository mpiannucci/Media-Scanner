Media-Scanner
=============

Python media scanner

A post download script used in conjunction with the transmission-daemon bittorent client.

<h2>Dependencies</h2>
<ul>
  <li>Python 2.7</li>
  <li>transmissionrpc python module</li>
  <li>transmission-daemon</li>
  <li>xbmc tools</li>
</ul>

<h2>Instructions</h2>
<ul>
  <li>Download the transmission-daemon</li>
  <li>Set the daemon to run as a service</li>
  
  <li>Modify the init.d script to run the program as root.</li>
  <li>Change the owner of the setting files to root</li>
  <li>Stop the service</li>
  <li>Set the configuration for the web and rpc interfaces</li>
  <li>Set the download folder and remember its path</li>
  <li>Set script-on-finish to true and the path to TorrentFinished as the file location</li>
  <li>Restart the service</li>
  <li>Set variables in scanner.py script as they apply to you</li>
  <li>Added a torrect via rpc or web interface and test!</li>
</ul>
  
