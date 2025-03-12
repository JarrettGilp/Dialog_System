using System.Collections;
using System.Collections.Generic;
using Microsoft.Unity.VisualStudio.Editor;
using TMPro;
using UnityEngine;

public class DialogBoxController : MonoBehaviour
{
    public GameObject backgroundImage, dialogTextBox;
    public Vector2 padding = new Vector2(20f, 10f);

    public TextMeshProUGUI dialogText;
    private RectTransform backgroundRect;

    public bool subsOn;

    [SerializeField] DialogOptionController optionController;

    private void Awake()
    {
        dialogText = dialogTextBox.GetComponent<TextMeshProUGUI>();
        backgroundRect = backgroundImage.GetComponent<RectTransform>();

        backgroundImage.SetActive(false);
        dialogTextBox.SetActive(false);
    }

    // Update is called once per frame
    void Update()
    {
        //subsOn = optionController.GetSubsOn();

        if( backgroundImage.activeSelf )
        {
            UpdateBackgroundSize();
        }
    }

    private void UpdateBackgroundSize()
    {
        float textWidth = dialogText.preferredWidth;
        float textHeight = dialogText.preferredHeight;

        backgroundRect.sizeDelta = new Vector2(textWidth + padding.x, textHeight + padding.y);
    }

    public void SetDialog(string text)
    {    
        subsOn = optionController.GetSubsOn();

        if( subsOn )
        {
            DialogBoxOn();
        }
        else{
            HideDialog();
        }

        dialogText.text = text;
        UpdateBackgroundSize();
    }

    public void DialogBoxOn()
    {
        dialogTextBox.SetActive(true);
        backgroundImage.SetActive(true);
    }

    public void HideDialog()
    {  
        dialogTextBox.SetActive(false);
        backgroundImage.SetActive(false);
    }

}
