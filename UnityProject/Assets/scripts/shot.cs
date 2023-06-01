using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class shot : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    public KeyCode screenShotButton;
	void Update()
	{
		if (Input.GetKeyDown(screenShotButton))
		{
			StartCoroutine(TakeScreenShot());
		}
	}
	void On_Click()
	{
		
	}
	
	IEnumerator TakeScreenShot()
	{
		yield return new WaitForEndOfFrame();
		ScreenCapture.CaptureScreenshot("screenshot.png");
	}
}
