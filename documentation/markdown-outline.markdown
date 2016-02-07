# Storyboard

This will be the story board. 

You can view the raw information to see how this is formatted by clicking `raw` on the top left of this file. 

## Code

```python
for i in range(20):
    print(i)
```

There is some code

## Images

Here is an image with a markdown image tag - 

![img](http://i.imgur.com/KoT1wEU.png)

Here's the code used for that image - 

```markdown
![img](http://i.imgur.com/KoT1wEU.png)
```

You can also use HTML `<img>` for keeping the image sizes consistent. Some of
the images on the story board (and other places probably) use this. 

Here's the code used for one of them : 

```html 
<img src= "https://raw.githubusercontent.com/geo7/vrbh_sim/develop/documentation/imgs/storyboard-imgs/robo3.png" data-canonical-src= "https://raw.githubusercontent.com/geo7/vrbh_sim/develop/documentation/imgs/storyboard-imgs/robo3.png" width="400" height="400" />
```

**NOTE** it all has to be one line iirc, so while it might be nicer to write as

```html
<img src= 
"https://raw.githubusercontent.com/geo7/vrbh_sim/develop/documentation/imgs/storyboard-imgs/robo3.png" 
data-canonical-src= 
"https://raw.githubusercontent.com/geo7/vrbh_sim/develop/documentation/imgs/storyboard-imgs/robo3.png" 
width="400" height="400" />
```

You would have to then concatenate the lines onto one. 

I have made a snippet for adding images which you may find useful - 

```html
<img src=
<ENTER IMG PATH IN QUOTES>
data-canonical-src=
<ENTER IMG PATH IN QUOTES>
width="400" height="400" />
```

So using that I would place the image path (in quotes) where it says, then
concatenate everything onto one line.

 
## Bold italic

Are done with `*` such as **bold** and *italic*

## URLS 

linked with `[` stuff

[here's a hyperlink](www.google.com)

******
