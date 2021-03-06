# composync

we're a students' project from the department [Cross Disciplinary Strategies](https://cdslab.uni-ak.ac.at/) at the [University of Applied Arts Vienna](https://dieangewandte.at/en)

we're currently in a pre-alpha stage, testing/usage on your own risk. get in contact if you're interested --> [florian.schinnerl@gmail.com](mailto:florian.schinnerl@gmail.com) !



### mission statement
> Our mission is to foster emotional learning  
> and exploration through the use of atmospheres,  
> composed of sound and visuals.  
> We are doing this using affective computing  
> as well as user generated input to feed an algorithm  
> which composes said atmospheres as well as to gather information  
> on how different atmospheres are emotionally received.  




### pre-requisits
you must have node.js and vue.js installed, as well as supercollider
- [tutorial for installing node.js](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Express_Nodejs/development_environment#installing_node)
- to install vue.js, type ```$ npm install vue```
- [download supercollider](https://supercollider.github.io/download)

### setup
1) start node server
  - on terminal in sc-slider/scr type ```node api.js```
2) start vue website
  - on terminal in sc-slider type ```npm run serve```
3) run supercollider script
  - open the .scd file in supercollider
  - run the first block by pressing cmd+enter at the opening or closing bracket 
  - run the second block by pressing cmd+enter at the opening or closing bracket 
4) open the website at http://localhost:8080/
  - move ball around
  - hear the music changing


### goals for setup
#### setup abstract
![composync setup](https://github.com/floschinnerl/composync/blob/main/composync-loop.gif)
#### tech setup
![composync tech setup](https://github.com/floschinnerl/composync/blob/main/tech-illustration.gif)
