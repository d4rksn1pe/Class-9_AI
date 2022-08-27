# The Rock Paper Scissors Game

![[game-screenshot.png]]

## Intro
It's a game based on the user's data (playing style) and predicts the next move of the person according to it. It gets trained as we play it. So, we are doing 2 things at once:
- Playing a game and having fun
- Training the AI for better predictions and gameplay
It uses CV too for better move recognisation (more ahead)

## Process
The game starts by asking permission for the camera. It ues the camera for recognition of our hand and the symbols we make from it. For this process, it uses the CV (Computer Vision) component of AI. 
If we don't want to play through our camera, we can play either through our mouse or keyboard. As we play, the machine is gathering data about us and making better predictions. We can notice this as you play longer. 

## Observation
The more we play, the more the machine/model gets trained for better predictions. It can then use this data pattern for playing with other players strategically.

## Learning
Machines can be trained as much as we want and they become more powerful as we train them. At one point, they become more powerful than us. 
Also, an AI Model can use 2 or more components of AI together as we see in this example where it's using both prediction and Computer Vision.

## Conclusion
It predicts the future moves by getting trained on our previous moves and creating a data pattern/graph. This graph can then also be used against other players resulting in a strong and strategic gameplay.