import numpy as np


plane = NumberPlane()
pi_creature  = PiCreature(color = PINK)
plane.prepare_for_nonlinear_transformation()
plane.add(pi_creature)

def homotopy(x,y,z,t):
	norm = np.linalg.norm([x,y])
	tau = interpolate(5,-5,t)+ norm/SPACE_WIDTH
    alpha = sigmoid(tau)
    return [x, y+0.5*np.sin(2*np.pi*alpha), z]

play(homotopyAnimation(homotopy, plane, run_time = 3))
dither(2)
play(MatrixTransfromation([[2,1], [1,2]], plane))
