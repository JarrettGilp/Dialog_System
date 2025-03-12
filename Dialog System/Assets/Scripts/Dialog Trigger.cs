using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Events;

public class DialogTrigger : MonoBehaviour
{
    public UnityEvent dialogFill;
    public UnityEvent dialogHide;

    void OnTriggerEnter(Collider other)
    {
        if( other.CompareTag("Player") )
        {
            dialogFill.Invoke();
        }
    }

    void OnTriggerExit(Collider other)
    {
        dialogHide.Invoke();
    }

}
