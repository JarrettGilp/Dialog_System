using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TempRailScript : MonoBehaviour
{
    [SerializeField] GameObject player;
    [SerializeField] GameObject point1;

    public float speed = 2f;

    // Start is called before the first frame update
    void Start()
    {
        StartCoroutine(MoveToPoint(player, point1));
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    IEnumerator MoveToPoint(GameObject playerObj, GameObject target)
    {
        Transform playerTransform = playerObj.transform;
        Transform targetTransform = target.transform;

        while( Vector3.Distance(playerTransform.position, targetTransform.position) > 0.001f)
        {
            playerTransform.position = Vector3.Lerp(playerTransform.position, targetTransform.position, speed * Time.deltaTime);
            yield return null;
        }
        playerTransform.position = targetTransform.position;
    }
}
