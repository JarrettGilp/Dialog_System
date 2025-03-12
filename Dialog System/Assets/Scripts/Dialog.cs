using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;

public class Dialog : MonoBehaviour
{

    [SerializeField] DialogBoxController dialogBoxController;

    // Dialog Dictionary
    Dictionary<int, string> dialog = new Dictionary<int, string>
    {
        [1] = "<color=blue>SWAPy</color>: Hello, new recruit. My name is SWAPy, your tour guide of the ASU Mars Innovation Zone, or ASUMIZ!",
        [2] = "<color=blue>SWAPy</color>: Welcome to Mars!"
    };

    public void GetDialog(int key)
    {
        string returnDialog = dialog[key];

        Debug.Log("The return dialog is: " + returnDialog);

        dialogBoxController.SetDialog(returnDialog);
    }

    public void HideDialogTime(float time)
    {
        StartCoroutine(WaitForHideDialog(time));
    }

    IEnumerator WaitForHideDialog(float time)
    {
        yield return new WaitForSeconds(time);
        dialogBoxController.HideDialog();
    }


}
