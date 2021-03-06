class Node(object):

    def Class(self):
        """
        self.Class() -> Class of node.
        @return: Class of node.
        """
        # raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")
        return "%s(%r)" % (self.__class__, self.__dict__)

    def __getitem__(self):
        """
        x.__getitem__(y) <==> x[y]
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def __len__(self):
        """
        x.__len__() <==> len(x)
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def __reduce_ex__(self):
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def __repr__(self):
        """
        x.__repr__() <==> repr(x)
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def __str__(self):
        """
        x.__str__() <==> str(x)
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def addKnob(self, k):
        """
        self.addKnob(k) -> None.
        Add knob k to this node or panel.
        @param k: Knob.
        @return: None.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def allKnobs(self):
        """
        self.allKnobs() -> list
            Get a list of all knobs in this node, including nameless knobs.
            For example:
               >>> b = nuke.nodes.Blur()
           >>> b.allKnobs()
            @return: List of all knobs.
            Note that this doesn't follow the links for Link_Knobs
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def autoplace(self):
        """
        self.autoplace() -> None.
        Automatically place nodes, so they do not overlap.
        @return: None.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def bbox(self):
        """
        self.bbox() -> List of x, y, w, h.
        Bounding box of the node.
        @return: List of x, y, w, h.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def canSetInput(self, i, node):
        """
        self.canSetInput(i, node) -> bool
        Check whether the output of 'node' can be connected to input i.
        @param i: Input number.
        @param node: The node to be connected to input i.
        @return: True if node can be connected, False otherwise.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def channels(self):
        """
        self.channels() -> String list.
        List channels output by this node.
        @return: String list.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def clones(self):
        """
        self.clones() -> Number of clones.
        @return: Number of clones.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def connectInput(self, i, node):
        """
        self.connectInput(i, node) -> bool
        Connect the output of 'node' to the i'th input or the next available unconnected input. The requested input is tried first, but if it is already set then subsequent inputs are tried until an unconnected one is found, as when you drop a connection arrow onto a node in the GUI.
        @param i: Input number to try first.
        @param node: The node to connect to input i.
        @return: True if a connection is made, False otherwise.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def deepSample(self, c, x, y, n):
        """
        self.deepSample(c, x, y, n) -> Floating point value.
        Return pixel values from a deep image.
        This requires the image to be calculated, so performance may be very bad if this is placed into an expression in
        a control panel.
        @param c: Channel name.
        @param x: Position to sample (X coordinate).
        @param y: Position to sample (Y coordinate).
        @param n: Sample index (between 0 and the number returned by deepSampleCount() for this pixel, or -1 for the frontmost).
        @return: Floating point value.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def deepSampleCount(self, x, y):
        """
        self.deepSampleCount(x, y) -> Integer value.
        Return number of samples for a pixel on a deep image.
        This requires the image to be calculated, so performance may be very bad if this is placed into an expression in
        a control panel.
        @param x: Position to sample (X coordinate).
        @param y: Position to sample (Y coordinate).
        @return: Integer value.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def dependencies(self, what):
        """
        self.dependencies(what) -> List of nodes.
            List all nodes referred to by this node. 'what' is an optional integer (see below).
        You can use the following constants or'ed together to select what types of dependencies are looked for:
                 nuke.EXPRESSIONS = expressions
                 nuke.INPUTS = visible input pipes
                 nuke.HIDDEN_INPUTS = hidden input pipes.
        The default is to look for all types of connections.
            Example:
        nuke.toNode('Blur1').dependencies( nuke.INPUTS | nuke.EXPRESSIONS )
        @param what: Or'ed constant of nuke.EXPRESSIONS, nuke.INPUTS and nuke.HIDDEN_INPUTS to select the types of dependencies. The default is to look for all types of connections.
        @return: List of nodes.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def dependent(self, what, forceEvaluate):
        """
        self.dependent(what, forceEvaluate) -> List of nodes.
            List all nodes that read information from this node.  'what' is an optional integer:
                 You can use any combination of the following constants or'ed together to select what types of dependent nodes to look for:
                         nuke.EXPRESSIONS = expressions
                         nuke.INPUTS = visible input pipes
                         nuke.HIDDEN_INPUTS = hidden input pipes.
        The default is to look for all types of connections.
            forceEvaluate is an optional boolean defaulting to True. When this parameter is true, it forces a re-evaluation of the entire tree.
        This can be expensive, but otherwise could give incorrect results if nodes are expression-linked.
            Example:
        nuke.toNode('Blur1').dependent( nuke.INPUTS | nuke.EXPRESSIONS )
        @param what: Or'ed constant of nuke.EXPRESSIONS, nuke.INPUTS and nuke.HIDDEN_INPUTS to select the types of dependent nodes. The default is to look for all types of connections.
        @param forceEvaluate: Specifies whether a full tree evaluation will take place. Defaults to True.
        @return: List of nodes.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def error(self):
        """
        error() -> bool
        True if the node or any in its input tree have an error, or False otherwise.
            Error state of the node and its input tree.  Deprecated; use hasError or treeHasError instead.
        Note that this will always return false for viewers, which cannot generate their input trees.  Instead, choose an input of the viewer (e.g. the active one), and call treeHasError() on that.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def fileDependencies(self, start, end):
        """
        self.fileDependencies(start, end) -> List of nodes and filenames.
            @param start: first frame
        @param end: last frame
        Returns the list of input file dependencies for this node and all nodes upstream from this node for the given frame range.
        The file dependencies are calcuated by searching for Read ops or ops with a File knob.
        All views are considered and current proxy mode is used to decide on whether full format or proxy files are returned.
        Note that Write nodes files are also included but precomps, gizmos and external plugins are not.
        Any time shifting operation such as frameholds, timeblurs, motionblur etc are taken into consideration.
        @return The return list is a list of nodes and files they require.
        Eg.  [Read1, ['file1.dpx, file2.dpx'] ], [Read2, ['file3.dpx', 'file4.dpx'] ] ]
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def firstFrame(self):
        """
        self.firstFrame() -> int.
        First frame in frame range for this node.
        @return: int.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def forceValidate(self):
        """
        self.forceValidate() -> None
            Force the node to validate itself, updating its hash.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def format(self):
        """
        self.format() -> Format.
        Format of the node.
        @return: Format.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def frameRange(self):
        """
        self.frameRange() -> FrameRange.
        Frame range for this node.
        @return: FrameRange.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def fullName(self):
        """
        self.fullName() -> str
        Get the name of this node and any groups enclosing it in 'group.group.name' form.
        @return: The fully-qualified name of this node, as a string.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def getNumKnobs(self):
        """
        self.numKnobs() -> The number of knobs.
        @return: The number of knobs.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def hasError(self):
        """
        hasError() -> bool
        True if the node itself has an error, regardless of the state of the ops in its input tree, or False otherwise.
            Error state of the node itself, regardless of the state of the ops in its input tree.
        Note that an error on a node may not appear if there is an error somewhere in its input tree, because it may not be possible to validate the node itself correctly in that case.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def height(self):
        """
        self.height() -> int.
        Height of the node.
        @return: int.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def help(self):
        """
        self.help() -> str
        @return: Help for the node.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def hideControlPanel(self):
        """
        self.hideControlPanel() -> None
        @return: None
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def input(self, i):
        """
        self.input(i) -> The i'th input.
        @param i: Input number.
        @return: The i'th input.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def inputs(self):
        """
        self.inputs() -> Gets the maximum number of connected inputs.
        @return: Number of the highest connected input + 1. If inputs 0, 1, and 3 are connected, this will return 4.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def isSelected(self):
        """
        self.isSelected() -> bool
            Returns the current selection state of the node.  This is the same as checking the 'selected' knob.
        @return: True if selected, or False if not.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def knob(self, p):
        """
        self.knob(p) -> The knob named p or the pth knob.
        @param p: A string or an integer.
        @return: The knob named p or the pth knob.
            Note that this follows the links for Link_Knobs
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def knobs(self):
        """
        self.knobs() -> dict
            Get a dictionary of (name, knob) pairs for all knobs in this node.
            For example:
               >>> b = nuke.nodes.Blur()
           >>> b.knobs()
            @return: Dictionary of all knobs.
            Note that this doesn't follow the links for Link_Knobs
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def lastFrame(self):
        """
        self.lastFrame() -> int.
        Last frame in frame range for this node.
        @return: int.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def linkableKnobs(self):
        """
        self.linkableKnobs(knobType) -> List
            Returns a list of any knobs that may be linked to from the node as well as some meta information about the knob. This may include whether the knob is enabled and whether it should be used for absolute or relative values. Not all of these variables may make sense for all knobs..
        @param knobType A KnobType describing the type of knobs you want.@return: A list of LinkableKnobInfo that may be empty .
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def maxInputs(self):
        """
        self.maximumInputs() -> Maximum number of inputs this node can have.
        @return: Maximum number of inputs this node can have.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def maxOutputs(self):
        """
        self.maximumOutputs() -> Maximum number of outputs this node can have.
        @return: Maximum number of outputs this node can have.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def maximumInputs(self):
        """
        self.maximumInputs() -> Maximum number of inputs this node can have.
        @return: Maximum number of inputs this node can have.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def maximumOutputs(self):
        """
        self.maximumOutputs() -> Maximum number of outputs this node can have.
        @return: Maximum number of outputs this node can have.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def metadata(self, key, time, view):
        """
        self.metadata(key, time, view) -> value or dict
        Return the metadata item for key on this node at current output context, or at optional time and view.
        If key is not specified a dictionary containing all key/value pairs is returned.
        None is returned if key does not exist on this node.
        @param key: Optional name of the metadata key to retrieve.
        @param time: Optional time to evaluate at (default is taken from node's current output context).
        @param view: Optional view to evaluate at (default is taken from node's current output context).
        @return: The requested metadata value, a dictionary containing all keys if a key name is not provided, or None if the specified key is not matched.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def minInputs(self):
        """
        self.minimumInputs() -> Minimum number of inputs this node can have.
        @return: Minimum number of inputs this node can have.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def minimumInputs(self):
        """
        self.minimumInputs() -> Minimum number of inputs this node can have.
        @return: Minimum number of inputs this node can have.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def name(self):
        """
        self.name() -> str
        @return: Name of node.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def numKnobs(self):
        """
        self.numKnobs() -> The number of knobs.
        @return: The number of knobs.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def opHashes(self):
        """
        self.opHashes() -> list of int
            Returns a list of hash values, one for each op in this node.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def optionalInput(self):
        """
        self.optionalInput() -> Number of first optional input.
        @return: Number of first optional input.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def performanceInfo(self):
        """
        self.performanceInfo( category ) -> Returns performance information for this node. Performance timing must be enabled.
        @category: performance category ( optional ).A performance category, must be either nuke.PROFILE_STORE, nuke.PROFILE_VALIDATE, nuke.PROFILE_REQUEST or nuke.PROFILE_ENGINE The default is nuke.PROFILE_ENGINE which gives the performance info of the render engine.
        @return: A dictionary containing the cumulative performance info for this category, where:
        callCount = the number of calls made
        timeTakenCPU =  the CPU time spent in microseconds
        timeTakenWall = the actual time ( wall time ) spent in microseconds
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def pixelAspect(self):
        """
        self.pixelAspect() -> int.
        Pixel Aspect ratio of the node.
        @return: float.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def proxy(self):
        """
        self.proxy() -> bool
        @return: True if proxy is enabled, False otherwise.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def readKnobs(self, s):
        """
        self.readKnobs(s) -> None.
        Read the knobs from a string (TCL syntax).
        @param s: A string.
        @return: None.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def redraw(self):
        """
        self.redraw() -> None.
        Force a redraw of the node.
        @return: None.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def removeKnob(self, k):
        """
        self.removeKnob(k) -> None.
        Remove knob k from this node or panel. Throws a ValueError exception if k is not found on the node.
        @param k: Knob.
        @return: None.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def resetKnobsToDefault(self):
        """
        self.resetKnobsToDefault() -> None
            Reset all the knobs to their default values.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def running(self):
        """
        self.running() -> Node rendering when paralled threads are running or None.
        Class method.
        @return: Node rendering when paralled threads are running or None.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def sample(self, c, x, y, dx, dy, frame):
        """
        self.sample(c, x, y, dx, dy) -> Floating point value.
        Return pixel values from an image.
        This requires the image to be calculated, so performance may be very bad if this is placed into an expression in
        a control panel. Produces a cubic filtered result. Any sizes less than 1, including 0, produce the same filtered result,
        this is correct based on sampling theory. Note that integers are at the corners of pixels, to center on a pixel add .5 to both coordinates.
        If the optional dx,dy are not given then the exact value of the square pixel that x,y lands in is returned. This is also called 'impulse filtering'.
        @param c: Channel name.
        @param x: Centre of the area to sample (X coordinate).
        @param y: Centre of the area to sample (Y coordinate).
        @param dx: Optional size of the area to sample (X coordinate).
        @param dy: Optional size of the area to sample (Y coordinate).
        @param frame: Optional frame to sample the node at.
        @return: Floating point value.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def screenHeight(self):
        """
        self.screenHeight() -> int.
        Height of the node when displayed on screen in the DAG, at 1:1 zoom, in pixels.
        @return: int.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def screenWidth(self):
        """
        self.screenWidth() -> int.
        Width of the node when displayed on screen in the DAG, at 1:1 zoom, in pixels.
        @return: int.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def selectOnly(self):
        """
        self.selectOnly() -> None.
        Set this node to be the only selection, as if it had been clicked in the DAG.
        @return: None.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def setInput(self, i, node):
        """
        self.setInput(i, node) -> bool
        Connect input i to node if canSetInput() returns true.
        @param i: Input number.
        @param node: The node to connect to input i.
        @return: True if canSetInput() returns true, or if the input is already correct.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def setName(self, name, uncollide, updateExpressions):
        """
        self.setName(name, uncollide=True, updateExpressions=False) -> None
        Set name of the node and resolve name collisions if optional named argument 'uncollide' is True.
        @param name: A string.
        @param uncollide: Optional boolean to resolve name collisions. Defaults to True.
        @param updateExpressions: Optional boolean to update expressions in other nodes to point at the new name. Defaults to False.
        @return: None
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def setSelected(self, selected):
        """
        self.setSelected(selected) -> None.
        Set the selection state of the node.  This is the same as changing the 'selected' knob.
        @param selected: New selection state - True or False.
        @return: None.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def setTab(self, tabIndex):
        """
        self.setTab(tabIndex) -> None
        @param tabIndex: The tab to show (first is 0).
        @return: None
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def setXYpos(self, x, y):
        """
        self.setXYpos(x, y) -> None.
        Set the (x, y) position of node in node graph.
        @param x: The x position of node in node graph.
        @param y: The y position of node in node graph.
        @return: None.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def setXpos(self, x):
        """
        self.setXpos(x) -> None.
        Set the x position of node in node graph.
        @param x: The x position of node in node graph.
        @return: None.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def setYpos(self, y):
        """
        self.setYpos(y) -> None.
        Set the y position of node in node graph.
        @param y: The y position of node in node graph.
        @return: None.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def showControlPanel(self, forceFloat):
        """
        self.showControlPanel(forceFloat = false) -> None
        @param forceFloat: Optional python object. If it evaluates to True the control panel will always open as a floating panel. Default is False.
        @return: None
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def showInfo(self, s):
        """
        self.showInfo(s) -> None.
        Creates a dialog box showing the result of script s.
        @param s: A string.
        @return: None.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def shown(self):
        """
        self.shown() -> true if the properties panel is open. This can be used to skip updates that are not visible to the user.
        @return: true if the properties panel is open. This can be used to skip updates that are not visible to the user.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def treeHasError(self):
        """
        treeHasError() -> bool
        True if the node or any in its input tree have an error, or False otherwise.
            Error state of the node and its input tree.
        Note that this will always return false for viewers, which cannot generate their input trees.  Instead, choose an input of the viewer (e.g. the active one), and call treeHasError() on that.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def upstreamFrameRange(self, i):
        """
        self.upstreamFrameRange(i) -> FrameRange
        Frame range for the i'th input of this node.
        @param i: Input number.
        @return: FrameRange. Returns None when querying an invalid input.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def width(self):
        """
        self.width() -> int.
        Width of the node.
        @return: int.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def writeKnobs(self, i):
        """
        self.writeKnobs(i) -> String in .nk form.
        Return a tcl list. If TO_SCRIPT | TO_VALUE is not on, this is a simple list
        of knob names. If it is on, it is an alternating list of knob names
        and the output of to_script().
            Flags can be any of these or'd together:
        - nuke.TO_SCRIPT produces to_script(0) values
        - nuke.TO_VALUE produces to_script(context) values
        - nuke.WRITE_NON_DEFAULT_ONLY skips knobs with not_default() false
        - nuke.WRITE_USER_KNOB_DEFS writes addUserKnob commands for user knobs
        - nuke.WRITE_ALL writes normally invisible knobs like name, xpos, ypos
            @param i: The set of flags or'd together. Default is TO_SCRIPT | TO_VALUE.
        @return: String in .nk form.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def xpos(self):
        """
        self.xpos() -> X position of node in node graph.
        @return: X position of node in node graph.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")
