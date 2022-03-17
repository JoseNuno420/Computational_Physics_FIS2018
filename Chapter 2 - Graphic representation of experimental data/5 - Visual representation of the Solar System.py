#This problem was complex so I decided to disregard the time it would take each planet to complete a full lap around the Sun. Therefore, they are
#represented as all travelling with the same speed. To fix this problem we would have to adapt the orbit function to each planet.

class Planet:
    def __init__(self,color_of_body,planet_radius, position):
        self.body = vp.sphere(color=color_of_body, \
                                radius=planet_radius,\
                                pos=position, canvas=scene, make_trail=True,retain=20) #sphere representative of each planet
        self.position = position #planet position
    
    def orbit(self, theta, delta_time):
            new_position = vp.vector(np.cos(theta), np.sin(theta),0) #calculates new position after a movement of thetha degrees
            self.body.pos = self.body.pos + new_position* delta_time #new positition after delta_time
            

scene = vp.canvas(title="Model of the Solar System")

scene.select()


Sun_radius = 2.5 #Sun's radius is of about 700,000km, we scaled it down to a scale of around 1/280,000

#scaling the planets on a scale of 1/10,000 we obtain these values for their radius
#For Jupiter and Saturn the scale was of 1/50,000 to better visualize them

Mercury_radius = 0.2
Venus_radius = 0.6
Earth_radius =0.6
Mars_radius =0.3
Jupiter_radius =1.3
Saturn_radius =1.1

base = 1 #representative measure of an astronomical unit for orbit radius calculations


#orbit radius for all planets considering the table given in the exercise as well as the suns radius
Mercury_orbit_radius = 3.5 + 0.4*base
Venus_orbit_radius = 3.5 + 0.7*base
Earth_orbit_radius = 3.5 + base
Mars_orbit_radius = 3.5 + 1.5*base
Jupiter_orbit_radius=3.5 + 5.2*base
Saturn_orbit_radius =3.5 + 9.5*base



Sun = Planet(vp.color.yellow,Sun_radius,vp.vector(0,0,0))
Mercury = Planet(vp.color.orange,Mercury_radius,vp.vector(0,-Mercury_orbit_radius,0))
Venus = Planet(vp.color.cyan,Venus_radius,vp.vector(0,-Venus_orbit_radius,0))
Earth = Planet(vp.color.blue,Earth_radius,vp.vector(0,-Earth_orbit_radius,0))
Mars = Planet(vp.color.yellow,Mars_radius,vp.vector(0,-Mars_orbit_radius,0))
Jupiter = Planet(vp.color.magenta,Jupiter_radius,vp.vector(0,-Jupiter_orbit_radius,0))
Saturno= Planet(vp.color.purple,Saturn_radius,vp.vector(0,-Saturn_orbit_radius,0))

time = 0
while time < 10:
        delta_time = 0.11
        for theta in np.arange(0,2*np.pi,0.028):
            vp.rate(60)
            Mercury.orbit(theta,delta_time)
            Venus.orbit(theta,delta_time+0.01)
            Earth.orbit(theta,delta_time+0.02)
            Mars.orbit(theta,delta_time+0.03)
            Jupiter.orbit(theta,delta_time+0.12)
            Saturn.orbit(theta,delta_time+0.21)
        time += delta_time
