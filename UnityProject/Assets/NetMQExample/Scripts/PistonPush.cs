using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PistonPush : MonoBehaviour
{
	Rigidbody m_Piston;
	float Frc2 = 0.0f;
    // Start is called before the first frame update
    public void Start()
    {
		m_Piston = GameObject.Find("Piston").GetComponent<Rigidbody>();
		StartCoroutine(Pusing());
    }

    // Update is called once per frame
    void Update()
    {
        m_Piston.velocity = new Vector3(Frc2, m_Piston.velocity.y, m_Piston.velocity.z);
    }
	public IEnumerator Pusing()
	{
		Frc2 = 2.0f;
		yield return new WaitForSeconds (3.0f);
		Frc2 = -2.0f;
		yield return new WaitForSeconds (3.0f);
		Frc2 = 0.0f;
		
	}
}
