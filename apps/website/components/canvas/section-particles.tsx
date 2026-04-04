"use client"

import { useEffect, useRef } from "react"

interface SectionParticlesProps {
  mode?: "rise" | "drift" | "orbit"
  count?: number
  color?: { r: number; g: number; b: number }
  maxOpacity?: number
}

const CORAL = { r: 212, g: 99, b: 94 }

export function SectionParticles({
  mode = "drift",
  count = 30,
  color = CORAL,
  maxOpacity = 0.25,
}: SectionParticlesProps) {
  const canvasRef = useRef<HTMLCanvasElement>(null)

  useEffect(() => {
    const canvas = canvasRef.current
    if (!canvas) return
    const ctx = canvas.getContext("2d")
    if (!ctx) return

    let w = 0, h = 0, raf = 0, time = 0, visible = true, resizeTimer: ReturnType<typeof setTimeout>

    interface P {
      x: number; y: number; vx: number; vy: number
      r: number; opacity: number; phase: number; speed: number
    }

    let particles: P[] = []

    function resize() {
      const dpr = Math.min(window.devicePixelRatio || 1, 2)
      const rect = canvas!.parentElement!.getBoundingClientRect()
      w = rect.width; h = rect.height
      canvas!.width = w * dpr; canvas!.height = h * dpr
      canvas!.style.width = `${w}px`; canvas!.style.height = `${h}px`
      ctx!.setTransform(dpr, 0, 0, dpr, 0, 0)
      init()
    }

    function debouncedResize() {
      clearTimeout(resizeTimer)
      resizeTimer = setTimeout(resize, 150)
    }

    function init() {
      particles = []
      for (let i = 0; i < count; i++) {
        particles.push({
          x: Math.random() * w, y: Math.random() * h,
          vx: 0, vy: 0,
          r: Math.random() * 2 + 0.5,
          opacity: Math.random() * maxOpacity * 0.6 + maxOpacity * 0.2,
          phase: Math.random() * Math.PI * 2,
          speed: Math.random() * 0.5 + 0.2,
        })
      }
    }

    function draw() {
      if (!visible) return
      time += 0.016
      ctx!.clearRect(0, 0, w, h)
      for (const p of particles) {
        if (mode === "rise") {
          p.vy = -p.speed * 0.5
          p.vx = Math.sin(time + p.phase) * 0.3
        } else if (mode === "drift") {
          p.vx = Math.cos(time * 0.5 + p.phase) * p.speed * 0.4
          p.vy = Math.sin(time * 0.3 + p.phase) * p.speed * 0.3
        } else if (mode === "orbit") {
          const cx = w / 2, cy = h / 2
          const angle = time * p.speed * 0.15 + p.phase
          const rx = (w * 0.3 + p.phase * 40) * (0.5 + Math.sin(p.phase) * 0.5)
          const ry = (h * 0.3 + p.phase * 30) * (0.5 + Math.cos(p.phase) * 0.5)
          p.x = cx + Math.cos(angle) * rx
          p.y = cy + Math.sin(angle) * ry
        }
        if (mode !== "orbit") {
          p.x += p.vx; p.y += p.vy
          if (mode === "rise") {
            if (p.y < -10) { p.y = h + 10; p.x = Math.random() * w }
          } else {
            if (p.x < -20) p.x += w + 40; if (p.x > w + 20) p.x -= w + 40
            if (p.y < -20) p.y += h + 40; if (p.y > h + 20) p.y -= h + 40
          }
        }
        const pulse = Math.sin(time * 1.5 + p.phase) * 0.3 + 0.7
        const alpha = p.opacity * pulse
        const g = ctx!.createRadialGradient(p.x, p.y, 0, p.x, p.y, p.r * 5)
        g.addColorStop(0, `rgba(${color.r},${color.g},${color.b},${alpha * 0.4})`)
        g.addColorStop(1, `rgba(${color.r},${color.g},${color.b},0)`)
        ctx!.beginPath(); ctx!.arc(p.x, p.y, p.r * 5, 0, Math.PI * 2); ctx!.fillStyle = g; ctx!.fill()
        ctx!.beginPath(); ctx!.arc(p.x, p.y, p.r, 0, Math.PI * 2)
        ctx!.fillStyle = `rgba(${color.r},${color.g},${color.b},${alpha})`; ctx!.fill()
      }
      raf = requestAnimationFrame(draw)
    }

    // Pause animation when off-screen
    const observer = new IntersectionObserver(([entry]) => {
      visible = entry.isIntersecting
      if (visible && !raf) raf = requestAnimationFrame(draw)
    }, { threshold: 0 })
    observer.observe(canvas)

    resize()
    raf = requestAnimationFrame(draw)
    window.addEventListener("resize", debouncedResize)

    return () => {
      cancelAnimationFrame(raf)
      window.removeEventListener("resize", debouncedResize)
      clearTimeout(resizeTimer)
      observer.disconnect()
    }
  }, [mode, count, color, maxOpacity])

  return (
    <canvas
      ref={canvasRef}
      aria-hidden="true"
      role="presentation"
      className="absolute inset-0 w-full h-full pointer-events-none"
      style={{ display: "block" }}
    />
  )
}
