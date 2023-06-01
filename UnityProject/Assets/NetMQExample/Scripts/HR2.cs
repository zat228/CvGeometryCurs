using AsyncIO;
using NetMQ;
using NetMQ.Sockets;
using UnityEngine;
using System.Collections;
using System.Collections.Generic;
public class HR2 : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }
	
	public bool Run()
    {	
		ForceDotNet.Force(); // this line is needed to prevent unity freeze after one use, not sure why yet
        using (RequestSocket client = new RequestSocket())
        { 
            client.Connect("tcp://localhost:5555");
			Debug.Log("Sending screen2");
			client.SendFrame("screen2");
			// ReceiveFrameString() blocks the thread until you receive the string, but TryReceiveFrameString()
			// do not block the thread, you can try commenting one and see what the other does, try to reason why
			// unity freezes when you use ReceiveFrameString() and play and stop the scene without running the server
//                string message = client.ReceiveFrameString();
//                Debug.Log("Received: " + message);
			string message = null;
			bool gotMessage = false;
			while (true)
			{
				gotMessage = client.TryReceiveFrameString(out message); // this returns true if it's successful
				if (gotMessage && message == "OK"){
				Debug.Log("taken: OK");
				Debug.Log("continue working");
				gotMessage = false;
				client.SendFrame("");
				return true;
				}
				if (gotMessage && message == "NO"){
				Debug.Log("taken: NO");
				Debug.Log("Activating porsh");
				gotMessage = false;
				client.SendFrame("");
				return false;
				} 				
			}

        }

        NetMQConfig.Cleanup(); // this line is needed to prevent unity freeze after one use, not sure why yet
    }
}
