<gui name="test">

<mainapp name="Histogram GUI">

  <mainframe name="Histogram GUI" label="mainframe" >

    <menubar>

      <menu text="&amp;File">
	<menuitem text="&amp;Open histogram" tip="Open saved histogram data file" click-callback="OnOpenHistogramFile"/>

	<menuitem text="&amp;Save plot to file" tip="Save plot to an image file" click-callback="OnSaveFigure"/>

	<menuitem text="&amp;Load a toolset" tip="Load a toolset" click-callback="OnLoadToolset"/>

	<menuitem text="&amp;Exit" tip="Exit Histogram GUI" click-callback="OnExit"/>
      </menu>


      <menu label="toolsMenu" text="&amp;Tools"/>


      <menu text="&amp;Help">
	<menuitem text="&amp;Online Tutorial" tip="Open tutorial web page" click-callback="OnOnlineTutorial">
	</menuitem>
	<menuitem text="&amp;About" tip="About Histogram GUI" click-callback="OnAbout">
	</menuitem>
      </menu>
    </menubar>


    <splitter direction="horizontal" minimumPanelSize="100" sliderPosition="400">
      
      <splitter direction="vertical" minimumPanelSize="250">
	<panel label="listpanel" borderStyle="sunken">
	  <sizer ratios="[0,1]" border="5" direction="vertical">
	    Histograms
	    <listbox style="single choice" label="histogramList" selectionChange-callback="OnSelectHistogram" keydown-callback="OnKeyDownInListWindow">
	    </listbox>
	  </sizer>
	</panel>
	<panel label="graph" borderStyle="default">
	  <sizer ratios="[1]" border="5" >
	    <histogramfigure size="(4,3)" dpi="75" label="histogramfigure">
	    </histogramfigure>
	  </sizer>
	</panel>
      </splitter>
      
      <panel label="lower" borderStyle="sunken">
	<sizer ratios="[1]" border="5">
	  <pyshell keydown-callback="+OnKeyDownInShellWindow" locals="pyshell_locals" label="pythonshell">
	  </pyshell>
	</sizer>
      </panel>
      
    </splitter>    

  </mainframe>
</mainapp>

</gui>
