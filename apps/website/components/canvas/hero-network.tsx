"use client"

import { useEffect, useRef } from "react"

interface Particle {
  x: number
  y: number
  vx: number
  vy: number
  originX: number
  originY: number
  radius: number
  opacity: number
  phase: number
  wanderAngle: number
}

const CORAL = { r: 212, g: 99, b: 94 }
const PARTICLE_COUNT = 60
const CONNECTION_DIST = 150
const MOUSE_RADIUS = 220

export function HeroNetwork() {
  const canvasRef = useRef<HTMLCanvasElement>(null)
  const stateRef = useRef<{
    particles: Particle[]
    mouse: { x: number; y: number }
    w: number
    h: number
    time: number
    raf: number
  }>({
    particles: [],
    mouse: { x: -9999, y: -9999 },
    w: 0,
    h: 0,
    time: 0,
    raf: 0,
  })

  useEffect(() => {
    const canvas = canvasRef.current
    if (!canvas) return
    const ctx = canvas.getContext("2d")
    if (!ctx) return
    const s = stateRef.current

    function resize() {
      const dpr = Math.min(window.devicePixelRatio || 1, 2)
      const rect = canvas!.parentElement!.getBoundingClientRect()
      s.w = rect.width
      s.h = rect.height
      canvas!.width = s.w * dpr
      canvas!.height = s.h * dpr
      canvas!.style.width = `${s.w}px`
      canvas!.style.height = `${s.h}px`
      ctx!.setTransform(dpr, 0, 0, dpr, 0, 0)
    }

    function initParticles() {
      s.particles = []
      for (let i = 0; i < PARTICLE_COUNT; i++) {
        const x = Math.random() * s.w
        const y = Math.random() * s.h
        s.particles.push({
          x, y, originX: x, originY: y,
          vx: (Math.random() - 0.5) * 0.3,
          vy: (Math.random() - 0.5) * 0.3,
          radius: Math.random() * 2 + 1,
          opacity: Math.random() * 0.4 + 0.2,
          phase: Math.random() * Math.PI * 2,
          wanderAngle: Math.random() * Math.PI * 2,
        })
      }
    }

    function draw() {
      s.time += 0.016
      const { particles, mouse, w, h, time } = s
      ctx!.clearRect(0, 0, w, h)

      for (const p of particles) {
        p.wanderAngle += (Math.random() - 0.5) * 0.15
        p.vx += Math.cos(p.wanderAngle) * 0.02
        p.vy += Math.sin(p.wanderAngle) * 0.02
        const homeX = p.originX - p.x
        const homeY = p.originY - p.y
        p.vx += homeX * 0.0003
        p.vy += homeY * 0.0003
        const mdx = p.x - mouse.x
        const mdy = p.y - mouse.y
        const mdist = Math.sqrt(mdx * mdx + mdy * mdy)
        if (mdist < MOUSE_RADIUS && mdist > 1) {
          const force = (1 - mdist / MOUSE_RADIUS) * 1.5
          p.vx += (mdx / mdist) * force
          p.vy += (mdy / mdist) * force
        }
        p.vx *= 0.97
        p.vy *= 0.97
        const speed = Math.sqrt(p.vx * p.vx + p.vy * p.vy)
        if (speed > 1.2) { p.vx = (p.vx / speed) * 1.2; p.vy = (p.vy / speed) * 1.2 }
        p.x += p.vx
        p.y += p.vy
        if (p.x < -30) { p.x = w + 20; p.originX = p.x }
        if (p.x > w + 30) { p.x = -20; p.originX = p.x }
        if (p.y < -30) { p.y = h + 20; p.originY = p.y }
        if (p.y > h + 30) { p.y = -20; p.originY = p.y }
      }

      ctx!.lineWidth = 0.5
      for (let i = 0; i < particles.length; i++) {
        for (let j = i + 1; j < particles.length; j++) {
          const a = particles[i], b = particles[j]
          const dx = a.x - b.x, dy = a.y - b.y
          const distSq = dx * dx + dy * dy
          if (distSq < CONNECTION_DIST * CONNECTION_DIST) {
            const d = Math.sqrt(distSq)
            const alpha = (1 - d / CONNECTION_DIST) * 0.14
            ctx!.beginPath()
            ctx!.moveTo(a.x, a.y)
            ctx!.lineTo(b.x, b.y)
            ctx!.strokeStyle = `rgba(${CORAL.r},${CORAL.g},${CORAL.b},${alpha})`
            ctx!.stroke()
          }
        }
      }

      if (mouse.x > -999) {
        ctx!.lineWidth = 0.8
        for (const p of particles) {
          const dx = p.x - mouse.x, dy = p.y - mouse.y
          const dist = Math.sqrt(dx * dx + dy * dy)
          if (dist < MOUSE_RADIUS) {
            const alpha = (1 - dist / MOUSE_RADIUS) * 0.22
            ctx!.beginPath()
            ctx!.moveTo(mouse.x, mouse.y)
            ctx!.lineTo(p.x, p.y)
            ctx!.strokeStyle = `rgba(${CORAL.r},${CORAL.g},${CORAL.b},${alpha})`
            ctx!.stroke()
          }
        }
      }

      for (const p of particles) {
        const pulse = Math.sin(time * 1.8 + p.phase) * 0.25 + 0.75
        const a = p.opacity * pulse
        const g = ctx!.createRadialGradient(p.x, p.y, 0, p.x, p.y, p.radius * 5)
        g.addColorStop(0, `rgba(${CORAL.r},${CORAL.g},${CORAL.b},${a * 0.3})`)
        g.addColorStop(1, `rgba(${CORAL.r},${CORAL.g},${CORAL.b},0)`)
        ctx!.beginPath()
        ctx!.arc(p.x, p.y, p.radius * 5, 0, Math.PI * 2)
        ctx!.fillStyle = g
        ctx!.fill()
        ctx!.beginPath()
        ctx!.arc(p.x, p.y, p.radius, 0, Math.PI * 2)
        ctx!.fillStyle = `rgba(${CORAL.r},${CORAL.g},${CORAL.b},${a})`
        ctx!.fill()
      }

      s.raf = requestAnimationFrame(draw)
    }

    const onMove = (e: MouseEvent) => {
      const r = canvas!.getBoundingClientRect()
      s.mouse.x = e.clientX - r.left
      s.mouse.y = e.clientY - r.top
    }
    const onLeave = () => { s.mouse.x = -9999; s.mouse.y = -9999 }

    let resizeTimer: ReturnType<typeof setTimeout>
    const handleResize = () => {
      clearTimeout(resizeTimer)
      resizeTimer = setTimeout(() => { resize(); initParticles() }, 150)
    }

    resize()
    initParticles()
    s.raf = requestAnimationFrame(draw)
    window.addEventListener("resize", handleResize)
    canvas.addEventListener("mousemove", onMove)
    canvas.addEventListener("mouseleave", onLeave)

    return () => {
      cancelAnimationFrame(s.raf)
      clearTimeout(resizeTimer)
      window.removeEventListener("resize", handleResize)
      canvas.removeEventListener("mousemove", onMove)
      canvas.removeEventListener("mouseleave", onLeave)
    }
  }, [])

  return (
    <canvas
      ref={canvasRef}
      aria-hidden="true"
      role="presentation"
      className="absolute inset-0 w-full h-full"
      style={{ display: "block" }}
    />
  )
}
