using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Events;
using UnityEngine.UI;
using TMPro;

public class DialogOptionController : MonoBehaviour
{
    // Start is called before the first frame update
    public UnityEvent SubtitlesEnabled;
    public UnityEvent SubtitlesDisabled;

    public bool subsOn;
    [SerializeField] TextMeshProUGUI dialogText;


    void Start()
    {
        //subsOn = true;
        SetSubsOn(true);
        SubtitlesEnabled.Invoke();
    }

    void Update()
    {
        if( Input.GetKeyDown(KeyCode.E) )
        {
            //subsOn = !subsOn;
            subsOn = GetSubsOn();

            SetSubsOn(!subsOn);
            
            bool subtitlesOn = GetSubsOn();

            if( subtitlesOn )
            {
                SubtitlesEnabled.Invoke();
            }
            else{
                SubtitlesDisabled.Invoke();
            }

        }
    }

    public void SetSubsOn(bool subsOn)
    {
        this.subsOn = subsOn;
    }

    public bool GetSubsOn()
    {
        return subsOn;
    }

}
