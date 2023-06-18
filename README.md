# nginx-docker-compose-showIP
1. Create an app (web app) that prints the local IP to the browser (on HTTP - port 80) 
2. Create a load balancer based on a docker nginx image exposed on port 9090.
3. Create a docker compose that runs 3 instances of the app you created + the load balancer.
4. Open browser and check http://localhost:9090, verify you see different IP each refresh.
                                                             
