# Short exercise for PlayMakers details

## Happy colors

To evoke a happy feeling, I searched on the internet for colors associated with happiness. 
I founc four colors on this websites: https://www.linkedin.com/pulse/how-colour-affects-your-mood-happiness-paulomi-debnath-
So, I choose yellow, orange, pink and red.

## Color variants

### Euclidean distance
To recognize the color, I tried several methods.
First, I used the most straightforward approach by calculating the Euclidean distance between each of the four happy colors to see if the current pixel color is a variant of a happy color. The goal was to recognize light red as a happy color, even if it is not 100% red in the RGB code.

### CIE LAB
I found that this ,ethod was quite limited. So, I did some research and found a method using the CIE LAB color space.
However, this made the execution very slow, so I decid to abandon this approach.

Source: https://medium.com/@bhuwankhatiwada57/color-difference-estimation-using-cie-l-a-b-color-space-b415f97a6b94
