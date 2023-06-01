using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using NetMQ;
using NetMQ.Sockets;

public class SecondTrigger : MonoBehaviour
{
	public GameObject TargetObj;
    Rigidbody m_Rigidbody;
	Rigidbody m_Piston;
	private HR2 Requester;
	private PistonPush punish;
    float Frc = 2.5f;
	float Frc2 = 0.0f;
    // Start is called before the first frame update
    void Start()
    {
        m_Rigidbody = GameObject.Find("package").GetComponent<Rigidbody>();
		m_Piston = GameObject.Find("Piston").GetComponent<Rigidbody>();
    }

    // Update is called once per frame
    void Update()
    {   
        // m_Rigidbody.AddForce(transform.forward * Frc);
		//Debug.Log(m_Rigidbody.velocity);
        m_Rigidbody.velocity = new Vector3(m_Rigidbody.velocity.x, m_Rigidbody.velocity.y, Frc);
		m_Piston.velocity = new Vector3(Frc2, m_Piston.velocity.y, m_Piston.velocity.z);

    }
	
	void OnTriggerEnter(Collider other)
    {
        if(other.tag == "package"){
			StartCoroutine(ScreenFunc2());
        } 
    }
	public IEnumerator ScreenFunc2()
	{		
		yield return new WaitForSeconds (0.4f);
		RenderTexture renderTexture = RenderTexture.GetTemporary(1200, 1000, 24);
		RenderTexture.active = renderTexture;
			   
		Camera tCamera = GameObject.Find("SecondCamera").GetComponent<Camera>();
			   
		tCamera.targetTexture = renderTexture;
		tCamera.Render();
			   
		Texture2D screenShot = new Texture2D(820, 500);
		screenShot.ReadPixels(new Rect(300,400,850,500),0,0);
		screenShot.Apply();
			   
		byte[] bytes = screenShot.EncodeToPNG();
		string filename = "screenShotUpSecond.png";
		System.IO.File.WriteAllBytes(filename, bytes);
		Debug.Log("A screenshot was taken!");
		yield return new WaitForSeconds (2f);
		Frc = 0f;
		Requester = new HR2();
		punish = new PistonPush();
		if (Requester.Run()){
			Frc = 2.5f;
			NetMQConfig.Cleanup();
		} else {
			StartCoroutine(Pusing());
		}
	}
	public IEnumerator Pusing()
	{
		Frc2 = 2.0f;
		yield return new WaitForSeconds (2.2f);
		Frc2 = -2.0f;
		yield return new WaitForSeconds (1.6f);
		Frc2 = 0.0f;
		NetMQConfig.Cleanup();
	}
}
