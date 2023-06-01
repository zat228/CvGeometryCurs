using UnityEngine;

public class HelloClient : MonoBehaviour
{
    HelloRequester _helloRequester;

    void Start()
    {	
        _helloRequester = new HelloRequester();
        _helloRequester.Start();
    }
	void Update(){
	}

    void OnDestroy()
    {
        _helloRequester.Stop();
    }
}