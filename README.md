# Document Understanding API
* Input: Document uploaded by user
* Output: Information extracted with the identified location

## ENVIRONMENT
* python3.75

## Clone the Project
<pre>
git clone https://github.com/aarontong95/Document_Scan_API.git
</pre>

## Install the Packages
<pre>
pip install -r requirements.txt
</pre>

## Deploy the Service
<pre>
uvicorn main:app --host 0.0.0.0 --port 8000
</pre>

## Quick Deploy with Docker
<pre>
docker-compose up
</pre>

## Get Started
<pre>
Go to http://127.0.0.1:8000/docs
Expand the row of "scan"
Click the "Try it out" button
Click the "Choose file" button
Upload the image 
</pre>


## Result
![alt text](https://github.com/aarontong95/Document_Scan_API/blob/main/pic/result.png)
