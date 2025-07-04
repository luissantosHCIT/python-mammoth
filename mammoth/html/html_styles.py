"""
    Style definitions simulating specific styles defined in Microsoft Word following the OpenOfficeXML documentation.
    Not all style definitions are correct or proper. I paid more attention to the ones I cared most.
    If you find a style is not sufficient, update this file to reflect a better simulation of the MS styles.
    I attempt to organize the styles by dictionaries with the key being the token string found in the XML and the
    value being the CSS result that should be injected in the HTML output.
"""

"""
    All possible WordML shapes below. For now, I only define a select few.
    See `DrawingML <http://officeopenxml.com/drwSp-prstGeom.php>`_

    accentBorderCallout1
    accentBorderCallout2
    accentBorderCallout3
    accentCallout1
    accentCallout2
    accentCallout3
    actionButtonBackPrevious
    actionButtonBeginning
    actionButtonBlank
    actionButtonDocument
    actionButtonEnd
    actionButtonForwardNext
    actionButtonHelp
    actionButtonHome
    actionButtonInformation
    actionButtonMovie
    actionButtonReturn
    actionButtonSound
    arc
    bentArrow
    bentConnector2
    bentConnector3
    bentConnector4
    bentConnector5
    bentUpArrow
    bevel
    blockArc
    borderCallout1
    borderCallout2
    borderCallout3
    bracePair
    bracketPair
    callout1
    callout2
    callout3
    can
    chartPlus
    chartStar
    chartX
    chevron
    chord
    circularArrow
    cloud
    cloudCallout
    corner
    cornerTabs
    cube
    curvedConnector2
    curvedConnector3
    curvedConnector4
    curvedConnector5
    curvedDownArrow
    curvedLeftArrow
    curvedRightArrow
    curvedUpArrow
    decagon
    diagStripe
    diamond
    dodecagon
    donut
    doubleWave
    downArrow
    downArrowCallout
    ellipse
    ellipseRibbon
    ellipseRibbon2
    flowChartAlternateProcess
    flowChartCollate
    flowChartConnector
    flowChartDecision
    flowChartDelay
    flowChartDisplay
    flowChartDocument
    flowChartExtract
    flowChartInputOutput
    flowChartInternalStorage
    flowChartMagneticDisk
    flowChartMagneticDrum
    flowChartMagneticTape
    flowChartManualInput
    flowChartManualOperation
    flowChartMerge
    flowChartMultidocument
    flowChartOfflineStorage
    flowChartOffpageConnector
    flowChartOnlineStorage
    flowChartOr
    flowChartPredefinedProcess
    flowChartPreparation
    flowChartProcess
    flowChartPunchedCard
    flowChartPunchedTape
    flowChartSort
    flowChartSummingJunction
    flowChartTerminator
    folderCorner
    frame
    funnel
    gear6
    gear9
    halfFrame
    heart
    heptagon
    hexagon
    homePlate
    horizontalScroll
    irregularSeal1
    irregularSeal2
    leftArrow
    leftArrowCallout
    leftBrace
    leftBracket
    leftCircularArrow
    leftRightArrow
    leftRightArrowCallout
    leftRightCircularArrow
    leftRightRibbon
    irregularSeal1
    leftRightUpArrow
    leftUpArrow
    lightningBolt
    line
    lineInv
    mathDivide
    mathEqual
    mathMinus
    mathMultiply
    mathNotEqual
    mathPlus
    moon
    nonIsoscelesTrapezoid
    noSmoking
    notchedRightArrow
    octagon
    parallelogram
    pentagon
    pie
    pieWedge
    plaque
    plaqueTabs
    plus
    quadArrow
    quadArrowCallout
    rect
    ribbon
    ribbon2
    rightArrow
    rightArrowCallout
    rightBrace
    rightBracket
    round1Rect
    round2DiagRect
    round2SameRect
    roundRect
    rtTriangle
    smileyFace
    snip1Rect
    snip2DiagRect
    snip2SameRect
    snipRoundRect
    squareTabs
    star10
    star12
    star16
    star24
    star32
    star4
    star5
    star6
    star7
    star8
    straightConnector1
    stripedRightArrow
    sun
    swooshArrow
    teardrop
    trapezoid
    triangle
    upArrow
    upArrowCallout
    upDownArrow
    upDownArrowCallout
    uturnArrow
    verticalScroll
    wave
    wedgeEllipseCallout
    wedgeRectCallout
    wedgeRoundRectCallout
"""
MS_SHAPES = {
    "rect": "clip-path: polygon(100% 100%,0% 100%,0% 0%,100% 0%);",
    "triangle": "clip-path: polygon(100% 100%,0% 100%,50% 0%);",
    "hexagon": "clip-path: polygon(93.30% 75%,50% 100%,6.70% 75%,6.70% 25%,50% 0%,93.30% 25%);",
    "diamond": "clip-path: polygon(100% 50%,50% 100%,0% 50%,50% 0.00%);",
    "roundRect": "clip-path: inset(0% 0% 0% 0% round 5%);",
    "circle": "clip-path: inset(0% 0% 0% 0% round 100%);",
    "rtTriangle": "clip-path: polygon(100% 100%,0% 100%,0% 0%,100% 100%);"
}

"""
    single - a single line
    dashDotStroked - a line with a series of alternating thin and thick strokes
    dashed - a dashed line
    dashSmallGap - a dashed line with small gaps
    dotDash - a line with alternating dots and dashes
    dotDotDash - a line with a repeating dot - dot - dash sequence
    dotted - a dotted line
    double - a double line
    doubleWave - a double wavy line
    inset - an inset set of lines
    nil - no border
    none - no border
    outset - an outset set of lines
    thick - a single line
    thickThinLargeGap - a thick line contained within a thin line with a large-sized intermediate gap
    thickThinMediumGap - a thick line contained within a thin line with a medium-sized intermediate gap
    thickThinSmallGap - a thick line contained within a thin line with a small intermediate gap
    thinThickLargeGap - a thin line contained within a thick line with a large-sized intermediate gap
    thinThickMediumGap - a thick line contained within a thin line with a medium-sized intermediate gap
    thinThickSmallGap - a thick line contained within a thin line with a small intermediate gap
    thinThickThinLargeGap - a thin-thick-thin line with a large gap
    thinThickThinMediumGap - a thin-thick-thin line with a medium gap
    thinThickThinSmallGap - a thin-thick-thin line with a small gap
    threeDEmboss - a three-staged gradient line, getting darker towards the paragraph
    threeDEngrave - a three-staged gradient like, getting darker away from the paragraph
    triple - a triple line
    wave - a wavy line
"""
MS_BORDER_STYLES = {
    'single': 'solid',
    'dashDotStroked': 'dashed dotted solid',
    'dashed': 'dashed',
    'dashSmallGap': 'dashed',
    'dotDash': 'dotted dashed',
    'dotDotDash': 'dotted dotted dashed',
    'dotted': 'dotted',
    'double': 'double',
    'doubleWave': 'double',
    'inset': 'inset',
    'nil': 'none',
    'none': 'none',
    'outset': 'outset',
    'thick': 'solid',
    'thickThinLargeGap': 'solid',
    'thickThinMediumGap': 'solid',
    'thickThinSmallGap': 'solid',
    'thinThickLargeGap': 'solid',
    'thinThickMediumGap': 'solid',
    'thinThickSmallGap': 'solid',
    'thinThickThinLargeGap': 'solid',
    'thinThickThinMediumGap': 'solid',
    'thinThickThinSmallGap': 'solid',
    'threeDEmboss': 'outset',
    'threeDEngrave': 'inset',
    'triple': 'solid',
    'wave': 'solid',
}

"""
Specifies the vertical alignment for text between the top and bottom margins of the cell. Possible values are:

    *. bottom - Specifies that the text should be vertically aligned to the bottom margin.
    *. center - Specifies that the text should be vertically aligned to the center of the cell.
    *. top - Specifies that the text should be vertically aligned to the top margin.
    
"""
MS_CELL_ALIGNMENT_STYLES = {
    'top': 'top',
    'center': 'middle',
    'bottom': 'bottom'
}

"""
See http://officeopenxml.com/prSlide-color.php
"""
OFFICE_THEME_COLORS = {
    "dark1": "000000",
    "dark2": "44546A",
    "light1": "FFFFFF",
    "light2": "E7E6E6",
    "accent1": "4472C4",
    "accent2": "ED7D31",
    "accent3": "A5A5A5",
    "accent4": "FFC000",
    "accent5": "5B9BD5",
    "accent6": "70AD47",
    "link": "0563C1",
    "followed_link": "954F72",
}
