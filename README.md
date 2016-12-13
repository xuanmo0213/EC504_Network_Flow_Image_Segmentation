### EC504 ImageSegmentation Project

Qiuxuan Lin, Yue Jin, Jingjing Zhu, Xiang Li, Yanjia Zhang

#### Environment setup:
* Install python, note that we are currently using some external packages such as numpy, sklearn.
 If you haven't done so, we recommend using [Anaconda](https://www.continuum.io/downloads), click through to install Python 2.7 version. For example, mac users:
 `bash Anaconda2-4.2.0-MacOSX-x86_64.sh `
* Install opencv using conda. You will first have to initialize conda in your command line
`export PATH=~/anaconda2/bin:$PATH`
then
`conda install -c https://conda.binstar.org/menpo opencv`

#### Make sure your have all the python packages at one directory:
1. image_process: include Gaussian Mixture and kmeans for likelihood score calculation
2. max_flow: core segmentation functions
3. main.py: driver program
Along with the zip we have also put a few toy images for test.

#### Now, in your commmand line
`~/anaconda2/bin/python main_2_0.py game.png`

Note that this is the absolute-correct-but-runs-slow version of our code. The program will prompt,
> Your image is in size 50 * 50
> Enter your desired scale ratio:

For game.png(50-by-50), we usually choose ratio = 2 to downsample it, then it takes about 20 secs to construct the adjacency list and 3 minutes (on our laptops) for max flow. When you are finished, mouse over to the pop-up windows, check the results and hit "return" to quit.

