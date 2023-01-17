# logic_api
This is a simple evaluator of a logic expression in a json format. The docker container will spin up a Fast API server on port 80.
To run the application:
1. Build the docker container 
```
docker build -t logic-api .
```
2. Run the image and forward the port.
```
docker run -p 80:80 logic-api
```
3. Test out the api with a curl command.
```
curl -X POST "http://127.0.0.1:80/evaluate"  -d '{"==":[1,1]}'
```