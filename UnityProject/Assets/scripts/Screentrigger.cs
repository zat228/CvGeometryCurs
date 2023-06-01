using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Screentrigger : MonoBehaviour
{	
	public int renderTexture_x;
	public int renderTexture_y;
	public int Texture2D_x;
	public int Texture2D_y;
	public int Rect_x1;
	public int Rect_y1;
	public int Rect_x2;
	public int Rect_y2;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }
	void OnTriggerEnter(Collider other)
    {
        if(other.tag == "package"){
			StartCoroutine(ScreenFunc());

        } 
    }
	private IEnumerator ScreenFunc()
	{		
		yield return new WaitForSeconds (0.4f);
		RenderTexture renderTexture = RenderTexture.GetTemporary(1200, 1000, 24);
		RenderTexture.active = renderTexture;
			   
		Camera tCamera = GameObject.Find("Camera").GetComponent<Camera>();
			   
		tCamera.targetTexture = renderTexture;
		tCamera.Render();
			   
		Texture2D screenShot = new Texture2D(820, 500);
		screenShot.ReadPixels(new Rect(300,400,850,500),0,0);
		screenShot.Apply();
			   
		byte[] bytes = screenShot.EncodeToPNG();
		string filename = "screenShotUp.png";
		System.IO.File.WriteAllBytes(filename, bytes);
		Debug.Log("A screenshot was taken!");
		
		RenderTexture renderTexture2 = RenderTexture.GetTemporary(renderTexture_x, renderTexture_y, 24);
		RenderTexture.active = renderTexture2;
		Camera tCamera2 = GameObject.Find("CameraLeft").GetComponent<Camera>();
			   
		tCamera2.targetTexture = renderTexture2;
		tCamera2.Render();
			   
		Texture2D screenShot2 = new Texture2D(Texture2D_x, Texture2D_y);
		screenShot2.ReadPixels(new Rect(Rect_x1,Rect_y1,Rect_x2,Rect_y2),0,0);
		screenShot2.Apply();
			   
		byte[] bytes2 = screenShot2.EncodeToPNG();
		string filename2 = "screenShotLeft.png";
		System.IO.File.WriteAllBytes(filename2, bytes2);
		Debug.Log("A screenshot was taken!");
	}
}
