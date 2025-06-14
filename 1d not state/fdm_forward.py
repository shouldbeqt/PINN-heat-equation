import numpy as np
import matplotlib.pyplot as plt

class HeatEquation:
    def __init__(self, T, alpha=0.1):
        self.L = 1.0      
        self.T = T          
        self.alpha = alpha 
        self.Nx = 10
        self.Nt = 100  
        
        self.dx = self.L / self.Nx
        self.dt = self.T / self.Nt
        
        # Проверка условия Куранта
        if self.alpha * self.dt / self.dx**2 > 0.5:
            raise ValueError("Условие Куранта не выполнено! Увеличьте Nt или уменьшите Nx.")
        
        self.heat_function = np.zeros((self.Nt, self.Nx))  
        self.set_boundary_conditions()
    
    def set_boundary_conditions(self):
        
        self.heat_function[0, :] = np.linspace(295, 295, self.Nx)
        
       
        self.heat_function[1:, 0] = 323  
        self.heat_function[1:, -1] = 323  
    
    def solve(self):
        for i in range(self.Nt - 1):
            for j in range(1, self.Nx - 1):
                self.heat_function[i+1, j] = self.heat_function[i, j] + self.alpha * self.dt / self.dx**2 * (
                    self.heat_function[i, j+1] - 2 * self.heat_function[i, j] + self.heat_function[i, j-1]
                )
        return self.heat_function 


heat_eq = HeatEquation(T=1.0)
final_temp = heat_eq.solve()

fig = plt.figure (figsize=(10, 7))
ax_3d = fig.add_subplot (projection = '3d')

x = np.linspace (0, 1, heat_eq.Nx)
t = np.linspace (0, 1 , heat_eq.Nt)

X, T = np.meshgrid (x,t)


ax_3d.plot_wireframe (X, T, final_temp)
ax_3d.set_xlabel ("coordinate")
ax_3d.set_ylabel ("time")
ax_3d.set_zlabel ("temperature")
plt.show ()

plt.figure(figsize=(10, 6))
plt.contourf(x, t, final_temp, levels=100, cmap='hot', alpha=0.8)
plt.colorbar(label='Temperature (°C)')
plt.title('Temperature Distribution Over Time')
plt.xlabel('Position (x)')
plt.ylabel('Time (ms)')

plt.show()