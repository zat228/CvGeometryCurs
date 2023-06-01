using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Move : MonoBehaviour
{
    Rigidbody m_Rigidbody;
    float Frc = 2.5f;
    // Start is called before the first frame update
    void Start()
    {
        m_Rigidbody = GetComponent<Rigidbody>();
    }

    // Update is called once per frame
    void Update()
    {   
        // m_Rigidbody.AddForce(transform.forward * Frc);
		//Debug.Log(m_Rigidbody.velocity);
        m_Rigidbody.velocity = new Vector3(m_Rigidbody.velocity.x, m_Rigidbody.velocity.y, Frc);

    }
	
}
