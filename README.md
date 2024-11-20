# To run the simulation:

Ensure Python and Pygame are installed on your system.
Save the provided Python scripts (agent1.py, agent2.py, environment.py, and run.py) in the same directory.
Open a terminal or command prompt, navigate to the directory containing the files, and execute:

**python run.py**

The simulation will display a grid with tasks (red squares) and barriers (black squares). Two buttons allow you to start simulations with Agent1 (A*) or Agent2 (UCS):
Click on the **A* Search** button to start Agent1's simulation.
Click on the **UCS Search** button to start Agent2's simulation.
The agents will navigate the grid to complete tasks while avoiding barriers.

**Observed Differences in Path Costs Between A* and UCS *

**A* (Agent1):*

-Uses the Manhattan distance as a heuristic for guiding path selection.
-Considers both path cost and estimated distance to the target, potentially finding shorter paths more quickly than UCS.
-Total path cost may be slightly lower in certain cases because of the heuristic's guidance.

**UCS (Agent2):**

-Uniform-cost search focuses solely on the actual path cost, without considering estimated distances.
-May take longer to find paths because it does not prioritize nodes based on proximity to the target.
-Total path cost is optimal in terms of distance traveled, but might involve exploring more nodes compared to A*.

**Observation during the simulation:**
When barriers or obstacles complicate direct paths, UCS often explores more alternatives than A*, which relies on heuristic guidance to reduce unnecessary exploration.


**Challenges Faced and Their Resolutions**
-Challenge 1: Synchronizing simulation logic between agents.
Resolution: Both agents follow similar move and find_path_to methods, but their pathfinding algorithms were separated to prevent interference. They share the same environment for consistency.

-Challenge 2: Handling real-time updates for tasks and barriers.
Resolution: Used a backup of the environment's initial state and restored it for each new simulation using deep copies, ensuring repeatable and consistent simulations.


