"use client"

import { useState, useEffect, useRef } from "react"

interface UseTypingEffectOptions {
  text: string
  speed?: number
  startDelay?: number
  enabled?: boolean
}

export function useTypingEffect({
  text,
  speed = 50,
  startDelay = 0,
  enabled = true,
}: UseTypingEffectOptions) {
  const [displayedText, setDisplayedText] = useState("")
  const indexRef = useRef(0)
  const intervalRef = useRef<ReturnType<typeof setInterval> | null>(null)

  const isComplete = displayedText.length === text.length

  useEffect(() => {
    if (!enabled) return

    indexRef.current = 0
    setDisplayedText("")

    const startTimeout = setTimeout(() => {
      intervalRef.current = setInterval(() => {
        indexRef.current += 1
        if (indexRef.current <= text.length) {
          setDisplayedText(text.slice(0, indexRef.current))
        } else {
          if (intervalRef.current) clearInterval(intervalRef.current)
          intervalRef.current = null
        }
      }, speed)
    }, startDelay)

    return () => {
      clearTimeout(startTimeout)
      if (intervalRef.current) clearInterval(intervalRef.current)
    }
  }, [text, speed, startDelay, enabled])

  return { displayedText, isComplete }
}
