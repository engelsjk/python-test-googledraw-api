# python-test-googledraw-api

The original purpose of this script is described in my writeup for the Google Quickdraw visualizer that I created.

<a href="https://github.com/engelsjk/web-demo-quickdraw-visualizer" target="_blank">https://github.com/engelsjk/web-demo-quickdraw-visualizer</a>

However, Google AI Experiments recently released another drawing tool, Autodraw. This new tool is a bit more functional than Quickdraw in that it tries to not only guess what you drew, but then offers to autocomplete your drawing by replacing it with a template of the same object. These templates or "stencils" are apparently curated by artists working with Google on these experiments.

I peaked behind the curtain of the new Autodraw tool and noticed some expected similarities to what I saw in Quickdraw. 

First off, the Autodraw tool is firing off requests to the 'inputtools' API as you draw, similar to the Quickdraw tool.

<code>https&#58;//inputtools.google.com/request?ime=handwriting&app=autodraw&dbg=1&cs=1&oe=UTF-8</code>

The API base URL is the same as the Quickdraw tool and the query string parameters are similar with the exception of 'app=autodraw' instead of 'app=quickdraw'. 

Additionally, the payload is similar in terms of structure, the primary difference being the "language":"autodraw" value. The "writing_guide" structure with the width/height of the drawing surface (or combined SVG elements?) and the "ink" array of x,y,t values is identical.

<code>{"input_type":0,"requests":[{"language":"autodraw","writing_guide":{"width":389.99999999999994,"height":533},"ink":[[[x],[y],[t]]]]}]}</code>

Out of curiousity, I ran the same ink array against the <code>inputtools.google.com</code> API, simply swapping out the app/language fields in each request. Somewhat surprisingly, the list of "guesses" and their associated scores are slightly different between apps. The list of scores below are the results from [Quickdraw, Autodraw], where a score of 0 indicates that the respective tool did not guess that object.

<code>
{u'belt': [8.4465789999999998, 5.1131152999999996],
 u'ceiling fan': [9.6525490000000005, 0],
 u'clarinet': [7.2248150000000004, 5.9660586999999996],
 u'diving board': [9.4369300000000003, 7.1665105999999996],
 u'dog': [9.8754220000000004, 6.2046099999999997],
 u'drill': [9.0572569999999999, 0],
 u'duck': [0, 7.3950110000000002],
 u'eyeglasses': [0, 6.7490315000000001],
 u'flamingo': [0, 7.5080523000000001],
 u'frying pan': [0, 7.2749844000000001],
 u'garden hose': [9.2187000000000001, 5.9557359999999999],
 u'giraffe': [7.5582231999999996, 5.5352297000000004],
 u'hockey stick': [9.5221999999999998, 0],
 u'key': [9.8502120000000009, 7.0177546],
 u'saxophone': [0.12961674000000001, 0.32083224999999999],
 u'shovel': [7.1525097000000004, 5.5746016999999997],
 u'snake': [9.4995639999999995, 7.6192570000000002],
 u'snorkel': [2.9602336999999999, 3.4037480000000002],
 u'sock': [7.8140916999999996, 3.8865327999999999],
 u'spoon': [8.5633545000000009, 6.3431839999999999],
 u'stethoscope': [0, 6.6366605999999999],
 u'swan': [2.7948647000000002, 1.7449923000000001],
 u'telephone': [8.0279875000000001, 0],
 u'toilet': [8.9421189999999999, 0],
 u'trombone': [5.4856075999999998, 4.6257023999999998]}
 </code>
 </br></br>
 
 Additionally, I noticed that there's a list of 'stencils' that is loaded as a JSON file on load of the Autodraw tool.
 
 <a href="https://autodraw.com/assets/stencils.json" target="_blank">https://autodraw.com/assets/stencils.json</a>
 
 This JSON file is a list of objects that appear to be the fixed set of guesses that can result from the machine-learning backend. For each object, there's a set of asset links to the SVG images that have been curated by various artists for this tool.
 
 For example, one of the assets for the guess of 'lion' has a URL of <a href="https://storage.googleapis.com/artlab-public.appspot.com/stencils/selman/lion-01.svg" target="_blank">https://storage.googleapis.com/artlab-public.appspot.com/stencils/selman/lion-01.svg</a>
 
 <img src="lion-01.svg" height="500px" width="auto">
 
 To date (Apr-14-2017), the <code>stencils.json</code> list only contains 371 objects, with between 1-19 assets for each object.
